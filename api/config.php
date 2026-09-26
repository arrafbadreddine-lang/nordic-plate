<?php
/**
 * Svenska Recept - Backend Configuration
 */
if (!defined('SVENSKA_RECEPT_APP')) {
    define('SVENSKA_RECEPT_APP', true);
}

// Admin Credentials - You can change this password anytime
define('ADMIN_PASSWORD', 'SvenskaRecept2026!');

// Session Settings
define('SESSION_NAME', 'svenska_admin_sess');
define('SESSION_LIFETIME', 86400 * 7); // 7 days

// Database Path (inside protected storage directory)
define('DB_PATH', dirname(__DIR__) . '/storage/reviews.db');

// Enable error reporting in development, disable in production if desired
error_reporting(E_ALL);
ini_set('display_errors', '0');
