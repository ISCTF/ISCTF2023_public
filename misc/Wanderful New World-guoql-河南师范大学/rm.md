## Wanderful New World

***

出题人：guoql

![image-20240414180336959](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240414180336959.png)

拿到我的世界存档直接开游戏，搜图后根据提示发现有一排方块，猜测为摩斯码进行替换成功得到一半 flag

![descript](C:/Users/26272/Pictures/media/7f56877f60be458f62362d097277f779.png)![descript](C:/Users/26272/Pictures/media/cf162225d5752cb711b0cea75a821efb.png)

另一半再搜寻后发现日志文件里存在特殊字符像 ASCII 码，转换后得到一串base64 再转换得到另一半 flag，两个一拼接得到完整 flag![descript](C:/Users/26272/Pictures/media/b59fd6d91a5c4f67c8591eee3af20e7b.png)

```
X01DX1dPUkxEX010X01TQ1RGfQ==
```

