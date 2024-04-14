#!/bin/sh
python3 -c "import os;FLAG=os.getenv('FLAG');REAL=''.join([chr(ord(i)-1) for i in FLAG]);f=open('/mfx_re.c','r');a=f.read();f.close();f=open('/mfx_re.c','w');f.write(a.replace('{{FLAG}}',REAL));f.close()"
FLAG="flag"
export FLAG="flag"
gcc mfx_re.c -o mfx_re
./upx mfx_re
mkdir /task
python3 -c "f=open('/mfx_re','rb');a=f.read();f.close();f=open('/task/mfx_re','wb');f.write(a.replace(b'UPX',b'MFX').replace(b'upx',b'mfx'));f.close()"
rm /upx
rm /mfx_re.c
rm /mfx_re
cd /task && python3 -m http.server