# fixes Apache 500 error
exec {'file_edit':
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}