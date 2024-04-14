## rsa_d

***

出题人：f00001111

![image-20240413225758742](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413225758742.png)

考点：RSA计算过程

入门题，根据RSA计算公式即可求出d，输入d后获得flag

```python
p=xxxxxxxx
q=xxxxxxxx
e=xxxxxxxx
phin=(p-1)*(q-1)
d=pow(e,-1,phin)

```



