# Create a file /tmp/school with permission 0744, file owner www-data,
# file group www-data and file content I love Puppet

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
