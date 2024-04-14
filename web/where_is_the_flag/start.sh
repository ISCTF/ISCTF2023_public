#!/bin/sh
sed -i "s/{{FLAG1}}/${FLAG:0:10}/" /var/www/localhost/htdocs/flag.php
echo ${FLAG:10:10} > /flag2
export FLAG3=${FLAG:20}
FLAG3=${FLAG:20}
export FLAG="flag"
FLAG="flag"
httpd -D FOREGROUND
