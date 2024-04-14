#!/bin/sh
echo $FLAG > /flaggggggg.txt
sed -i "s/zend.assertions = -1/zend.assertions = 1/g" /etc/php7/php.ini
export FLAG="flag"
FLAG="flag"
httpd -D FOREGROUND