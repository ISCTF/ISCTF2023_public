## 小蓝鲨的秘密

***

出题人：D0UBL3SEV3N

![image-20240413230801550](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413230801550.png)

考点：伪加密，png 高度,aes

压缩包载入 010，CTRL+f 搜索 50 4B 01 02 ，找到加密文件的全局标志位，将两个 09 都改成 00 如下：

![descript](C:/Users/26272/Pictures/media/eb292ce84412c7857826acc99c3bcb09.png)

改成 00 解除伪加密，然后 txt 文档打开看题目描述

![descript](C:/Users/26272/Pictures/media/4719955872c729a7e8daf1dc3cdfa64a.png)

得到一个字符串和一张蓝鲨图片。这个字符串看格式疑似 AES 加密。那么图片里可能隐藏着密 码。修改 png 图片的高度，将 10 修改为 83 得到密码

![descript](C:/Users/26272/Pictures/media/08baa187a91e211fd5ca8858b7cbce47.png)

![descript](C:/Users/26272/Pictures/media/44990947a52b890fdf2995e113e5643f.png)

密码为：15CTF2023

AES 在线解密： <https://tool.oschina.net/encrypt/>

![descript](C:/Users/26272/Pictures/media/51ab482ead509aa5655d3db40d0fa8a5.png)

得到 flag：

```
ISCTF{2832-3910-232-3742-7320}
```

