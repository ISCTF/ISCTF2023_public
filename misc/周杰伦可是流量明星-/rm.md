## 杰伦可是流量明星

***

出题人:fpclose

![image-20240413231108958](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413231108958.png)

下载附件，解压，发现一个 login.mp3，是一个音频文件，并且可以播放，但是却不是莫斯密码。使用 16进制工具打开发现：

![descript](C:/Users/26272/Pictures/media/20076c6f8aa869da3dedfe26328be845.png)

开头是一个rar的压缩包，将音频文件修改为：login.rar，解压发现文件中有一个流量文件 login.pcapng 。使用工具打开，发现有一个http流量包：

![descript](C:/Users/26272/Pictures/media/327e766f253549ffed4b776da3f160f4.png)

右键，追踪流的TCP流

![descript](C:/Users/26272/Pictures/media/44b3da4714fb381ec2fc40bfc57e5d8d.png)

打开发现flag：

![descript](C:/Users/26272/Pictures/media/b78a492c92655460f72666020103fa6d.png)

%7B是‘{’，%7D是‘}’，将中间的内容复制下来，放入isctf{},提交即可。

