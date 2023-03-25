# Kill a process named killmenow using the exec resource and pkill command

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
