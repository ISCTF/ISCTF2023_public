from secret import flag,key
from Crypto.Util.number import *
from Crypto.Cipher import AES
import os

assert(len(flag)==39)
assert(len(key)==16)

def padding(msg):
    tmp = 16 - len(msg)%16
    pad = hex(tmp)[2:].zfill(2)
    return bytes.fromhex(pad*tmp)+msg

def encrypt(message,key,iv):
    aes = AES.new(key,AES.MODE_CBC,iv=iv)
    enc = aes.encrypt(message)
    return enc

iv = os.urandom(16)
message = padding(flag)
hint = bytes_to_long(key)^bytes_to_long(message[:16])
enc = encrypt(message,key,iv)

print(enc)
print(hex(hint))

"""
b'bsF\xb6m\xcf\x94\x9fg1\xfaxG\xd4\xa3\x04\xfb\x9c\xac\xed\xbe\xc4\xc0\xb5\x899|u\xbf9e\xe0\xa6\xdb5\xa8x\x84\x95(\xc6\x18\xfe\x07\x88\x02\xe1v'
0x47405a4847405a48470000021a0f2870
"""