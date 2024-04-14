#!/bin/sh
sed -i "s/{{FLAG}}/$FLAG/" /var/www/localhost/htdocs/flag.php
export FLAG="flag"
FLAG="flag"
httpd -D FOREGROUND
