<?php
/*
Read /flaggggggg.txt
*/
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
highlight_file(__FILE__);

if(preg_match("/cat|tac|more|less|head|tail|nl|sed|sort|uniq|rev|awk|od|vi|vim/i", $_POST['code'])){//strings
    die("想读我文件？大胆。");
}
elseif (preg_match("/\^|\||\~|\\$|\%|jay/i", $_POST['code'])){
    die("无字母数字RCE？大胆！");
}
elseif (preg_match("/bash|nc|curl|sess|\{|:|;/i", $_POST['code'])){
    die("奇技淫巧？大胆！！");
}
elseif (preg_match("/fl|ag|\.|x/i", $_POST['code'])){
    die("大胆！！！");
}
else{
    assert($_POST['code']);
}