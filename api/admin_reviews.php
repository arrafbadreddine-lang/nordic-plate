<?php
/**
 * Svenska Recept - Admin Moderation API
 * Handles login, listing, approving, rejecting, and deleting reviews.
 */
header('Content-Type: application/json; charset=utf-8');
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/db.php';

session_name(SESSION_NAME);
session_set_cookie_params([
    'lifetime' => SESSION_LIFETIME,
    'path'     => '/',
    'secure'   => isset($_SERVER['HTTPS']),
    'httponly' => true,
    'samesite' => 'Lax'
]);
session_start();

$action = $_GET['action'] ?? $_POST['action'] ?? '';

// Check if authenticated
function is_admin_authenticated() {
    if (!empty($_SESSION['is_admin']) && $_SESSION['is_admin'] === true) {
        return true;
    }
    // Also allow bearer token or header password
    $headers = getallheaders();
    $auth_header = $headers['X-Admin-Password'] ?? $headers['x-admin-password'] ?? '';
    if (!empty($auth_header) && $auth_header === ADMIN_PASSWORD) {
        $_SESSION['is_admin'] = true;
        return true;
    }
    return false;
}

// 1. LOGIN
if ($action === 'login') {
    $raw_input = file_get_contents('php://input');
    $json = json_decode($raw_input, true);
    $password = $json['password'] ?? $_POST['password'] ?? '';

    if (!empty($password) && $password === ADMIN_PASSWORD) {
        $_SESSION['is_admin'] = true;
        echo json_encode(['success' => true, 'message' => 'Inloggad!']);
    } else {
        http_response_code(401);
        echo json_encode(['success' => false, 'error' => 'Felaktigt lösenord.']);
    }
    exit;
}

// 2. LOGOUT
if ($action === 'logout') {
    $_SESSION['is_admin'] = false;
    session_destroy();
    echo json_encode(['success' => true, 'message' => 'Utloggad.']);
    exit;
}

// 3. CHECK AUTH
if ($action === 'check') {
    echo json_encode(['authenticated' => is_admin_authenticated()]);
    exit;
}

// All subsequent actions require authentication
if (!is_admin_authenticated()) {
    http_response_code(401);
    echo json_encode(['success' => false, 'error' => 'Ej auktoriserad. Logga in först.']);
    exit;
}

$db = get_db_connection();
if (!$db) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Databasfel.']);
    exit;
}

// 4. LIST REVIEWS
if ($action === 'list') {
    $filter_status = $_GET['status'] ?? 'pending';
    if (!in_array($filter_status, ['pending', 'approved', 'rejected', 'all'])) {
        $filter_status = 'pending';
    }

    try {
        // Get counts
        $counts_query = $db->query("
            SELECT status, COUNT(*) as cnt 
            FROM reviews 
            GROUP BY status
        ");
        $counts = ['pending' => 0, 'approved' => 0, 'rejected' => 0, 'total' => 0];
        while ($row = $counts_query->fetch()) {
            $st = $row['status'];
            $c = (int)$row['cnt'];
            if (isset($counts[$st])) {
                $counts[$st] = $c;
            }
            $counts['total'] += $c;
        }

        // Fetch reviews
        if ($filter_status === 'all') {
            $stmt = $db->prepare("SELECT * FROM reviews ORDER BY created_at DESC LIMIT 200");
            $stmt->execute();
        } else {
            $stmt = $db->prepare("SELECT * FROM reviews WHERE status = :status ORDER BY created_at DESC LIMIT 200");
            $stmt->execute([':status' => $filter_status]);
        }
        $reviews = $stmt->fetchAll();

        echo json_encode([
            'success' => true,
            'counts'  => $counts,
            'filter'  => $filter_status,
            'reviews' => $reviews
        ]);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    }
    exit;
}

// Read review ID for mutation actions
$raw_input = file_get_contents('php://input');
$json = json_decode($raw_input, true);
$review_id = isset($json['id']) ? (int)$json['id'] : (isset($_POST['id']) ? (int)$_POST['id'] : 0);

if ($review_id <= 0) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Saknar giltigt recensions-ID.']);
    exit;
}

// 5. APPROVE
if ($action === 'approve') {
    try {
        $stmt = $db->prepare("
            UPDATE reviews 
            SET status = 'approved', updated_at = datetime('now') 
            WHERE id = :id
        ");
        $stmt->execute([':id' => $review_id]);
        echo json_encode(['success' => true, 'message' => 'Recension godkänd och publicerad!']);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    }
    exit;
}

// 6. REJECT
if ($action === 'reject') {
    try {
        $stmt = $db->prepare("
            UPDATE reviews 
            SET status = 'rejected', updated_at = datetime('now') 
            WHERE id = :id
        ");
        $stmt->execute([':id' => $review_id]);
        echo json_encode(['success' => true, 'message' => 'Recension avvisad.']);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    }
    exit;
}

// 7. DELETE
if ($action === 'delete') {
    try {
        $stmt = $db->prepare("DELETE FROM reviews WHERE id = :id");
        $stmt->execute([':id' => $review_id]);
        echo json_encode(['success' => true, 'message' => 'Recension raderad permanent.']);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    }
    exit;
}

http_response_code(400);
echo json_encode(['success' => false, 'error' => 'Okänd åtgärd.']);
