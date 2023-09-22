# Kills running process killmenow
exec {'kill_process':
  command  => 'pkill killmenow',
  provider => 'shell',
}
