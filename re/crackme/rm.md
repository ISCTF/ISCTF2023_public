## crackme

***

出题人：D0UBL3SEV3N

![image-20240413223656517](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223656517.png)

下载附件后拖入 Exeinfo PE 查壳

![descript](C:/Users/26272/Pictures/media/026d579852fb1ef02bc89f6985144b57.png)

首先看到是 upx 壳，但是提示不要尝试用 upx.exe -d 去脱：

![descript](C:/Users/26272/Pictures/media/73824f90b07410a502e969c95e681df7.png)

EP section 不对，是被改了，winhex 查看：

![descript](C:/Users/26272/Pictures/media/1967aa0e47b633f6e675d72649816d39.png)

改对应的 16 进制，让第一个 PFX0 变成 UPX0，第二个 PFX0 变成 UPX1，也就是把第一个 50 46 58 30 改成 55 50 58 30；第二个 50 46 58 30 改成 55 50 58 31 如下：

![descript](C:/Users/26272/Pictures/media/e54b1784193fd9ad0f61da38034dfc71.png)

再去查一下是否正常了

![descript](C:/Users/26272/Pictures/media/b0d18c4a6875756286309dd7a3658d2d.png)

显示正常，脱壳：

![descript](C:/Users/26272/Pictures/media/fa1f989cdfee33b2beaabf3e84986336.png)

然后载入 ida64 找到主函数

![descript](C:/Users/26272/Pictures/media/84ec6122ff27f03bce7ab709bc6ef7c0.png)

![descript](C:/Users/26272/Pictures/media/1a24b5a47ecda424399bfec2fa2a2d52.png)

反编译 拿到 flag

```
ISCTF{873c-298c-2948-23bh-291h-kt30}
```

这题有非预期，直接运行程序也能得到flag。