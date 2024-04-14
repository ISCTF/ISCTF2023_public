#!/bin/sh	#必需的东西没什么好讲的
sed -i "s/ISCTF{this_is_flag}/$FLAG/" /var/www/html/flag.txt #使用平台的动态flag替换

export FLAG=""

