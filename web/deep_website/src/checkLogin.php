<?php
session_start();
date_default_timezone_set('Asia/shanghai');

require_once "config.php";
require_once "waf.php";


function checkLogin($user,$password){
	$password = md5($password);
	$user = waf($user);
	$sql = "select describes from user where username=('$user') and passwd = ('$password')";
	$res = fetchOne($sql);
	if($res)
		return true;
	else
		return false;

}
$user = isset($_POST['user']) ? trim($_POST['user']) : null;
$password = isset($_POST['password']) ? trim($_POST['password']) : null;
$verifyCode = isset($_POST['verifyCode']) ? trim($_POST['verifyCode']) : null; 

$sessionVerifyCode = $_SESSION['verifyCode'];
if($verifyCode != $sessionVerifyCode)
{
	exit('验证码错误');
} 

if($user != null && $password !=null)
{
	if(checkLogin($user,$password))
	{
		setcookie('user',$user,time()+60*60,'','','',true);
		$_SESSION['user'] = $user;
		header('Location:main.php');
	}
	else
	{
		echo'用户名或密码错误！';
	}
}
else
{
	echo '用户名或密码不能为空';
}

?>
