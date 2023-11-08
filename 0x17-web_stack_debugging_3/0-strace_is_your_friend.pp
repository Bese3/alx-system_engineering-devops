# fixes Apache 500 error
exec {'file_edit'
    onlyif => "test -e /var/www/html/wp-settings.php",
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}