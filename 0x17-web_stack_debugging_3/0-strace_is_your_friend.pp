exec {'file_edit'
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}