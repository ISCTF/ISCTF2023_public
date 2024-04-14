<?php
include_once "config.php";
include_once "waf.php";

$UA = isset($_SERVER['HTTP_USER_AGENT']) ? trim($_SERVER['HTTP_USER_AGENT']) : null;
if($UA !== null){
	if(False !== stripos($UA, "sqlmap")){
		die("bad hacker!");
	}
}

if(isset($_POST['username'])){
	if(isset($_POST['password'])){
		$username = urldecode(waf($_POST['username']));
		$password = md5(urldecode(waf($_POST['password'])));
		$sql = "SELECT user FROM users WHERE user='$username' AND password='$password'";
		$row = fetchOne($sql);
		if($row){
			echo "用户$".$row['user']."\$登录成功";
		}
		else{
			echo "用户名或密码错误";
		}
	}
	else{
		die("not exists");
	}
}
else{
	die("not exists");
}

?>
