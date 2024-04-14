<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<link rel="stylesheet" type="text/css" href="./static/index.css">
</head>

<body>
<script type="text/javascript">

	function DealResponse(string){
		p = document.getElementById('response')
		p.innerHTML = string;
	}

	function login(username,password){
	var xmlhttp;
	if(window.XMLHttpRequest){
		xmlhttp = new XMLHttpRequest();
	}
	else{
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange = function(){
		if(xmlhttp.readyState === 4 && xmlhttp.status === 200){
		var responseText = xmlhttp.responseText;
		DealResponse(responseText);
		}
	};
	xmlhttp.open("POST","/check.php");
	xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
	var msg ="username=" + encodeURIComponent(username) + "&password=" + encodeURIComponent(password);
	xmlhttp.send(msg);
}

</script>

	<div id="login_box">
	<h2>LOGIN</h2>
	<div id="input_box">
		<input type="text" id="username" placeholder="请输入用户名">
	</div>
	<div class="input_box">
		<input type="password" id="password" placeholder="请输入密码">
	</div>
	<button onclick="login(document.getElementById('username').value,document.getElementById('password').value)">登录</button><br>
	<br>
	<p id="response" style="color: yellow;"></p>
	<br>
	</div>
</body>
</html>
