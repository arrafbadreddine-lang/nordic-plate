<?php
header('Content-Type: application/json');
require_once __DIR__ . '/config.php';

$res = [
    'php_version' => PHP_VERSION,
    'pdo_sqlite' => extension_loaded('pdo_sqlite'),
    'sqlite3' => extension_loaded('sqlite3'),
    'db_path' => DB_PATH,
    'dir_exists' => is_dir(dirname(DB_PATH)),
    'dir_writable' => is_writable(dirname(DB_PATH)),
    'file_exists' => file_exists(DB_PATH),
    'file_writable' => file_exists(DB_PATH) ? is_writable(DB_PATH) : false,
];

try {
    $pdo = new PDO('sqlite:' . DB_PATH);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->exec('CREATE TABLE IF NOT EXISTS test (id INT);');
    $res['connection'] = 'SUCCESS';
} catch (Exception $e) {
    $res['connection'] = 'FAILED';
    $res['error'] = $e->getMessage();
}

echo json_encode($res, JSON_PRETTY_PRINT);
