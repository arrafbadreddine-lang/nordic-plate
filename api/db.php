<?php
/**
 * Svenska Recept - Database Helper (SQLite3 via PDO)
 */
require_once __DIR__ . '/config.php';

function get_db_connection() {
    static $pdo = null;
    if ($pdo !== null) {
        return $pdo;
    }

    $db_file = DB_PATH;
    $db_dir = dirname($db_file);

    if (!is_dir($db_dir)) {
        mkdir($db_dir, 0755, true);
    }

    try {
        $pdo = new PDO('sqlite:' . $db_file);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

        // Enable WAL mode for high concurrency
        $pdo->exec('PRAGMA journal_mode = WAL;');

        // Create table if not exists
        $pdo->exec("
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_slug TEXT NOT NULL,
                recipe_title TEXT NOT NULL,
                author_name TEXT NOT NULL,
                author_email TEXT,
                rating INTEGER NOT NULL,
                comment TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                ip_address TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS idx_reviews_slug_status ON reviews(recipe_slug, status);
            CREATE INDEX IF NOT EXISTS idx_reviews_status ON reviews(status);
        ");

        return $pdo;
    } catch (PDOException $e) {
        error_log('Database Connection Error: ' . $e->getMessage());
        return null;
    }
}
