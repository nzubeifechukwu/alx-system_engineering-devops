file { '/root/.ssh/config':
  ensure  => 'file',
  content => 'Host\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no',
}
