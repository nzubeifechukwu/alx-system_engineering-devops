# Configure OS so user holberton can log in and open files without error

# Boost hard limit for holberton user
exec { 'boost-hard-limit-for-user-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Boost soft limit for holberton user
exec { 'boost-soft-limit-for-user-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
