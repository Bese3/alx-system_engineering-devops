# Configures a server to act as a load balancer for 2 web servers
exec {'configure_haproxy':
	command => './0-custom_http_response_header',
	provider => 'shell'
}
