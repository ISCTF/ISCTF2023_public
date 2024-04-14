## easy_z3
***

该题灵感源自朝雾师傅给sh的题目ease_math

![image-20240413223732513](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223732513.png)

出题人：her01st

解题工具:

python
z3-solver

```python
from z3 import *   
l=['']*20
for i in range(6):
    l[i]=Int('l['+str(i)+']')
s=Solver()
s.add((593*l[5] + 997*l[0] + 811*l[1] + 258*l[2] + 829*l[3] + 532*l[4])== 0x54eb02012bed42c08)
s.add((605*l[4] + 686*l[5] + 328*l[0] + 602*l[1] + 695*l[2] + 576*l[3])== 0x4f039a9f601affc3a)
s.add((373*l[3] + 512*l[4] + 449*l[5] + 756*l[0] + 448*l[1] + 580*l[2])== 0x442b62c4ad653e7d9)
s.add((560*l[2] + 635*l[3] + 422*l[4] + 971*l[5] + 855*l[0] + 597*l[1])== 0x588aabb6a4cb26838)
s.add((717*l[1] + 507*l[2] + 388*l[3] + 925*l[4] + 324*l[5] + 524*l[0])== 0x48f8e42ac70c9af91)
s.add((312*l[0] + 368*l[1] + 884*l[2] + 518*l[3] + 495*l[4] + 414*l[5])== 0x4656c19578a6b1170)

if s.check()==sat:
    m=s.model()
flag=""
for i in range(6):
    p=hex(m[l[i]].as_long())[2:]
    for j in range(int(len(p)/2)):
        flag+=chr(int(p[j*2:j*2+2],16))
print(flag)

```

```
ISCTF{N0_One_kn0ws_m@th_B3tter_Th@n_me!!!}
```