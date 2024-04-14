#!/bin/sh
echo $FLAG > /flag
chmod 644 /flag
export FLAG="flag"
FLAG="flag"

export FLAG=not_flag
apache2-foreground
