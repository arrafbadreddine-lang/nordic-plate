<?php
/**
 * Svenska Recept - Public Review Submission Endpoint
 * POST /api/submit_review.php
 */
header('Content-Type: application/json; charset=utf-8');
require_once __DIR__ . '/db.php';

// Only allow POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method Not Allowed']);
    exit;
}

// Read inputs from JSON or POST data
$raw_input = file_get_contents('php://input');
$json_data = json_decode($raw_input, true);

$data = is_array($json_data) ? $json_data : $_POST;

// 1. Spam Honeypot Check (field should remain empty)
if (!empty($data['website_hp']) || !empty($data['phone_check'])) {
    // Fake success response to confuse spambots
    echo json_encode(['success' => true, 'message' => 'Tack för din recension!']);
    exit;
}

// 2. Extract and Sanitize Inputs
$recipe_slug  = isset($data['recipe_slug']) ? trim(strip_tags($data['recipe_slug'])) : '';
$recipe_title = isset($data['recipe_title']) ? trim(strip_tags($data['recipe_title'])) : '';
$author_name  = isset($data['author_name']) ? trim(strip_tags($data['author_name'])) : '';
$author_email = isset($data['author_email']) ? trim(strip_tags($data['author_email'])) : '';
$rating       = isset($data['rating']) ? (int)$data['rating'] : 5;
$comment      = isset($data['comment']) ? trim(strip_tags($data['comment'])) : '';

// 3. Validation
$errors = [];

if (empty($recipe_slug) || !preg_match('/^[a-z0-9\-]+$/', $recipe_slug)) {
    $errors[] = 'Ogiltigt recept identifierare.';
}

if (empty($recipe_title)) {
    $recipe_title = ucwords(str_replace('-', ' ', $recipe_slug));
}
if (mb_strlen($recipe_title) > 200) {
    $recipe_title = mb_substr($recipe_title, 0, 200);
}

if (empty($author_name) || mb_strlen($author_name) < 2) {
    $errors[] = 'Vänligen ange ett giltigt namn (minst 2 tecken).';
}
if (mb_strlen($author_name) > 60) {
    $author_name = mb_substr($author_name, 0, 60);
}

if (!empty($author_email)) {
    if (!filter_var($author_email, FILTER_VALIDATE_EMAIL) || mb_strlen($author_email) > 100) {
        $errors[] = 'Vänligen ange en giltig e-postadress.';
    }
}

if ($rating < 1 || $rating > 5) {
    $rating = 5;
}

if (empty($comment) || mb_strlen($comment) < 4) {
    $errors[] = 'Vänligen skriv en kommentar om receptet (minst 4 tecken).';
}
if (mb_strlen($comment) > 2000) {
    $comment = mb_substr($comment, 0, 2000);
}

if (!empty($errors)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => implode(' ', $errors)]);
    exit;
}

// 4. Rate Limiting (max 10 submissions per IP per hour)
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';
$db = get_db_connection();
if (!$db) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Databasfel. Försök igen senare.']);
    exit;
}

try {
    $throttle_stmt = $db->prepare("
        SELECT COUNT(*) as count 
        FROM reviews 
        WHERE ip_address = :ip 
          AND created_at >= datetime('now', '-1 hour')
    ");
    $throttle_stmt->execute([':ip' => $ip]);
    $row = $throttle_stmt->fetch();
    if ($row && (int)$row['count'] >= 10) {
        http_response_code(429);
        echo json_encode(['success' => false, 'error' => 'För många förfrågningar från samma adress. Försök igen senare.']);
        exit;
    }

    // 5. Insert into Database as 'pending'
    $stmt = $db->prepare("
        INSERT INTO reviews (recipe_slug, recipe_title, author_name, author_email, rating, comment, status, ip_address, created_at, updated_at)
        VALUES (:slug, :title, :name, :email, :rating, :comment, 'pending', :ip, datetime('now'), datetime('now'))
    ");
    $stmt->execute([
        ':slug'   => $recipe_slug,
        ':title'  => $recipe_title,
        ':name'   => $author_name,
        ':email'  => $author_email,
        ':rating' => $rating,
        ':comment'=> $comment,
        ':ip'     => $ip
    ]);

    echo json_encode([
        'success' => true,
        'message' => 'Tack! Din recension har tagits emot och publiceras så snart den granskats av redaktionen. ⭐'
    ]);
} catch (Exception $e) {
    error_log('Error saving review: ' . $e->getMessage());
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Kunde inte spara recensionen just nu.']);
}
