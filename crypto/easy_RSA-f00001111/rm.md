## easy_rsa

***

出题人：f00001111

![image-20240413225627635](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413225627635.png)

考点：RSA计算过程

入门题，根据RSA计算公式求出flag

```python
p=xxxxxxxxxx
q=xxxxxxxxxx
e=xxxxxxxxxx
c=xxxxxxxxxx
n=p*q
phin=(p-1)*(q-1)
d=pow(e,-1,phin)
m=pow(c,d,n)

```

