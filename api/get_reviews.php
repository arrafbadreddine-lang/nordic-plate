<?php
/**
 * Svenska Recept - Public Approved Reviews Endpoint
 * GET /api/get_reviews.php?slug=klassiska-saftiga-kardemummabullar
 */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=60'); // 60s browser/CDN cache
require_once __DIR__ . '/db.php';

$slug = isset($_GET['slug']) ? trim(strip_tags($_GET['slug'])) : '';

if (empty($slug) || !preg_match('/^[a-z0-9\-]+$/', $slug)) {
    echo json_encode(['success' => true, 'slug' => '', 'count' => 0, 'reviews' => []]);
    exit;
}

$db = get_db_connection();
if (!$db) {
    echo json_encode(['success' => true, 'slug' => $slug, 'count' => 0, 'reviews' => []]);
    exit;
}

try {
    $stmt = $db->prepare("
        SELECT id, author_name, rating, comment, created_at
        FROM reviews
        WHERE recipe_slug = :slug 
          AND status = 'approved'
        ORDER BY created_at DESC
        LIMIT 50
    ");
    $stmt->execute([':slug' => $slug]);
    $rows = $stmt->fetchAll();

    $swedish_months = [
        '01' => 'jan', '02' => 'feb', '03' => 'mar', '04' => 'apr',
        '05' => 'maj', '06' => 'jun', '07' => 'jul', '08' => 'aug',
        '09' => 'sep', '10' => 'okt', '11' => 'nov', '12' => 'dec'
    ];

    $reviews = [];
    foreach ($rows as $r) {
        $timestamp = strtotime($r['created_at']);
        $day = date('j', $timestamp);
        $month_num = date('m', $timestamp);
        $month_str = $swedish_months[$month_num] ?? date('M', $timestamp);
        $year = date('Y', $timestamp);
        $date_formatted = "$day $month_str $year";

        $reviews[] = [
            'id'       => (int)$r['id'],
            'name'     => htmlspecialchars($r['author_name'], ENT_QUOTES, 'UTF-8'),
            'rating'   => (int)$r['rating'],
            'comment'  => htmlspecialchars($r['comment'], ENT_QUOTES, 'UTF-8'),
            'date'     => $date_formatted,
            'verified' => true
        ];
    }

    echo json_encode([
        'success' => true,
        'slug'    => $slug,
        'count'   => count($reviews),
        'reviews' => $reviews
    ]);
} catch (Exception $e) {
    error_log('Error fetching reviews: ' . $e->getMessage());
    echo json_encode(['success' => true, 'slug' => $slug, 'count' => 0, 'reviews' => []]);
}
