#!/bin/sh
echo $FLAG > /real_flag
export FLAG="flag"
FLAG="flag"
httpd -D FOREGROUND