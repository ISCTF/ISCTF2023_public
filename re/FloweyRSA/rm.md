## FloweyRSA

***

出题人：Laffey

![image-20240413224130255](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224130255.png)

IDA一打开连main函数都没了。

![descript](C:/Users/26272/Pictures/media/2281327082f8b977abe90f6de6510ae0.png)

往下翻，有几个地方是必然发生的跳转指令，中间是一坨花指令。全部nop掉

![descript](C:/Users/26272/Pictures/media/8f3295e24ec300710b4f110ced4969da.png)

![descript](C:/Users/26272/Pictures/media/c09733d417373788dae43ed5f8c16716.png)

然后在main应该开始的地方create function

![descript](C:/Users/26272/Pictures/media/3701487ea99ab16a63da7b6c4e17c1d3.png)

就能f5了。

![descript](C:/Users/26272/Pictures/media/124491a4fc6145b0d5efb4b860432fe9.png)

发现是RSA加密。把密文挑出来

![descript](C:/Users/26272/Pictures/media/39bbbc28907dc15fcc9bfbfb9b125a88.png)

公钥很小，随便分解。

```python
from Crypto.Util.number import*
e=0o721
p=56099
q=56369
n=p*q
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
ca=[0x00000000753C2EC5, 0x000000008D90C736, 0x0000000081282CB0,0x000000007EECC470, 0x00000000944E15D3, 0x000000002C7AC726, 0x00000000717E8070,0x0000000030CBE439, 0x00000000B1D95A9C, 0x000000006DB667BB, 0x000000001240463C,0x0000000077CBFE64, 0x0000000011D8BE59]
flag=b''
for c in ca:
    m=pow(c,d,n)
    flag+=long_to_bytes(m)
print(flag)

```

![descript](C:/Users/26272/Pictures/media/bef9fe185a9b3388cb5eba401673b449.png)

![descript](C:/Users/26272/Pictures/media/a2337cb85753d05077a42ad270fc9b6a.png)

```
flag{reverse_is_N0T_@lways_jusT_RE_myy_H@bIb1!!!!!!}
```

