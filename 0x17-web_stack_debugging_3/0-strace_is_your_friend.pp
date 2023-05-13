# Resolve and fix 500 error from Apache web server

$path_to_file_to_edit = '/var/www/html/wp-settings.php'

# Replace phpp with php in /var/www/html/wp-settings.php
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${path_to_file_to_edit}",
  path    => ['/bin','/usr/bin']
}
