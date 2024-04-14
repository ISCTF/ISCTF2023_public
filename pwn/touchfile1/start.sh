#!/bin/sh
# Add your startup script
sed -i "s/ISCTF{this_is_flag}/$FLAG/" /home/ctf/flag #使用平台的动态flag替换

export FLAG=""
FLAG = ""
# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
