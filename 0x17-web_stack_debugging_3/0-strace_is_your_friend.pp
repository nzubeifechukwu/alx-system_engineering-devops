# Resolve and fix 500 error from Apache web server

# Replace phpp with php in /var/www/html/wp-settings.php
exec {
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin']
}
