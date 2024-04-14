#!/bin/sh
sed -i "s/{{FLAG}}/$FLAG/" /var/www/localhost/htdocs/index.php
export FLAG="flag"
FLAG="flag"
mysql_install_db
create_user=`cat <<EOF
USE mysql;
FLUSH PRIVILEGES;
CREATE DATABASE bthcls;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY "bthcls" WITH GRANT OPTION;
FLUSH PRIVILEGES;
EOF`
echo "$create_user" | mysqld --bootstrap
init_sql=`cat /tmp/init.sql`
echo "$init_sql" | mysqld --bootstrap
mysqld_safe --nowatch
httpd -D FOREGROUND