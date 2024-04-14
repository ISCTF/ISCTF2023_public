<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>管理员后台</title>
<style>
        canvas {
        position: fixed;
        right: 0px;
        bottom: 0px;
        min-width: 100%;
        min-height: 100%;
        height: auto;
        width: auto;
        z-index: -1;
        }
        *{
            padding: 0;
            margin: 0;
            text-decoration: none;
        }
        body{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-size: 110%;
        }
        .login{
            width: 550px;
            height: 400px;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(
                to right bottom,
                rgba(255,255,255,.4),
                rgba(255,255,255,.4),
                rgba(255,255,255,.4)
            );
            /*使背景模糊化*/
            backdrop-filter: blur(10px);
            box-shadow: 0 0 20px #3d3d3d;
            border-radius: 15px;
        } 

        .table{
            font: 900 40px '';
            text-align: center;
            letter-spacing: 5px;
            color: #3d3d3d;
        }

        .box{
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .box input{
            width: 400px;
            height: 100%;
            margin-bottom: 20px;
            outline: none;
            border: 0;
            padding: 10px;
            background-color: transparent;
            border-bottom: 3px solid rgb(150, 150, 240);
            font: 900 16px '';
        }

        .go{
            text-align: center;
            display: block;
            height: 24px;
            width: 400px;
            padding: 12px;
            font: 900 20px '';
            border-radius: 10px;
            margin-top: 20px;
            color: #fff;
            letter-spacing: 3px;
            background-image: linear-gradient(to left,
            #3d3d3d);
        }
    </style>
</head>
<body>
<canvas style="background:#111" id="canvas" width="1440" height="900" ></canvas>
<script type="text/javascript" src="/js/DigitalRain.js"></script>
<script type="text/javascript" src="/js/sm4.js"></script>
<form id="form1" name="form1" method="post" action="#" >
<div class="login">
  <div class="box">
  <p class="table">后台</p>
  <br>
  <input type="text" name="username" placeholder="用户名">
  <input type="password" name="password" placeholder="密码">
  <br>
  <input class="go" type="submit" name="submit" value="登录"/>
<?php
error_reporting(0);
$link = mysqli_connect("localhost", "root", "bthcls", "bthcls",3306);

function waf($str){

    if (preg_match("/union|\=|\+|sleep|benchmark|for|where|sys|innodb|null|like|\/\*|\*\//i",$str)){
        die("<h4>illegal words!</h4>");
    }
    return $str;
}

if(isset($_POST['username']) && isset($_POST['password']))
{
    
    $username = $_POST['username'];
    $password = $_POST['password'];

    $username = waf($username);
    $password = waf($password);


    // 尝试选择查询执行
    $sql="SELECT user,username, password FROM users WHERE username='$username' and password='$password'";

    $result = mysqli_query($link, $sql);

    $row = mysqli_fetch_array($result);

    if($row)
    {

        $result = mysqli_query($link, $sql);
        if (mysqli_num_rows($result) > 0) 
        {
            
            if($username == "admin" && $password == "we1come7o1sctf"){
                echo "{{FLAG}}";
            }
            
            else{
                while($row = mysqli_fetch_assoc($result)) 
                {

                    echo "You are so smart! Let me give you a hint ↓ 5aSn5L2s77yM5L2g6L+Z5LmI6IGq5piO5bqU6K+l5LiN6ZyA6KaBaGludOWQpz8=";
                    die();
                }
            }
            // 输出数据
            
        }
    } 
    else{
            echo "<h4>用户名或密码错误!</h4>";
        }
}

// Close connection 关闭连接
mysqli_close($link);
?>
  </div>
</div>
</form>
<!-- sqlmap是没有灵魂的 -->
</body>
</html>
