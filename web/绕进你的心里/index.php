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