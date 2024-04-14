#!/bin/sh

# Get the user
user=$(ls /home)

#!/bin/sh
sed -i "s/{{FLAG}}/$FLAG/" /var/www/html/flag.php
export FLAG="flag"
FLAG="flag"


chmod +x /var/www/html/flag.php

php-fpm &

nginx &

echo "Running..."

tail -F /dev/null
