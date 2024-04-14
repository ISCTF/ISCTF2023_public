<?php

session_start();

/* 
生成随机数
*/
function buildRandomText($type = 3,$langth = 4)
{
    switch($type)
    {
        case 1:
            $text = join(range(0,9));
            break;
        case 2:
            $text = join(array_merge(range('a','z'),range('A','Z')));
            break;
        case 3;
            $text = join(array_merge(range('a','z'),range('A','Z'),range(0,9)));
            break;
    }
    $text = str_shuffle($text);
    $text = substr($text,0,$langth);
    return $text;
}

$img = imagecreatetruecolor(110,40);    //新建一个真彩色图像 创建背景
$white = imagecolorallocate($img,255,255,255);  //创建一个颜色
imagefilledrectangle($img,0,0,110,40,$white);   //给矩形填充 
$red = imagecolorallocate($img,255,0,0);

$dir= dirname(__FILE__);    //获取绝对路径
$text = buildRandomText(); 
$_SESSION['verifyCode'] = $text;
$i=0;
while($i < strlen($text))
{
    $size = mt_rand(15,25);
    $angle = mt_rand(-15,15);
    $x = 10 + $i*mt_rand(20,25);
    $y = mt_rand(28,32);
    $color = imagecolorallocate($img,mt_rand(0,255),mt_rand(0,255),mt_rand(0,255));
    imagettftext($img,$size,$angle,$x,$y,$color,$dir.'/'.'font/ARIALBD.TTF',$text[$i]); //向图像写入文本
    $i++;
}

$i=0;
while($i<3)
{
    $color = imagecolorallocate($img,mt_rand(0,255),mt_rand(0,255),mt_rand(0,255));
    imageline($img,mt_rand(0,110),mt_rand(0,40),mt_rand(0,110),mt_rand(0,40),$color);
    $i++;
}

//echo buildRandomText();

header('Content-Type:image/jpeg');  //将输出形式改为图像形式

imagejpeg($img);    //将图像输出到浏览器

?>