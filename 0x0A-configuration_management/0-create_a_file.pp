# Creates a file with some content and specified group, owner and file mode
file {'/tmp/school':
    ensure  => file,
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
