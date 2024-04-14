<?php
session_start();
date_default_timezone_set('Asia/shanghai');


?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>沃特伐商品管理系统后台</title>
	<link rel="stylesheet" type="text/css" href="./static/index.css">
</head>

<body>
	<div class="loginBox">
		<h2>login</h2>
		<form action="checkLogin.php" method="post">
			<div class="item">
				<input type="text" name="user" required>
				<label for="">userName</label>
			</div>
			<div class="item">
				<input type="password" name="password" required>
				<label for="">password</label>
			</div>
			<div class="item">
				<input type="text" name="verifyCode" required>
				<label for="">verifyCode</label>
				<img src="verifyCode.php">
			</div>
			<button class="btn">submit
				<span></span>
				<span></span>
				<span></span>
				<span></span>
			</button>
		</form>
	</div>
</body>
</html>
