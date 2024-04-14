## 你说爱我?尊嘟假嘟?

***

出题人：D0UBL3SEV3N

![image-20240413230017792](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413230017792.png)

考点：Ook 加密，base64

附件是个 docx 文档，打开后重复出现 “你说爱我” “尊嘟” “假嘟”。判断为 Ook 加密,将 “你说爱我”替换为“Ook.”；“尊嘟”替换为：“Ook!”；“假嘟”替换为：“Ook?”。注 意替换的时候中英文符号即可。 然后 Ook 解码：

![descript](C:/Users/26272/Pictures/media/1955df7d96ca6cb733183589684fbfcf.png)

得到一个字符串：ild3l4pXejwPcCwJsPAOq7sJczdRdTsJcCEUsP1Z

base64 解码,注意编码方式不同，要切换一下：

![descript](C:/Users/26272/Pictures/media/e61cf0bebfbb55a8a94f09ac84b6c5b4.png)

```
ISCTF{9832h-s92hw-23u7w-2j8s0}
```

