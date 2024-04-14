<?php
    include "utils/function.php";
    $config = include  "utils/config.php";
    $username = $_REQUEST['username'];
    $password = $_REQUEST['password'];
    if(empty($username)||empty($password)) die("Username or password cannot be empty XD");
    if(!is_user_exists($username, $config["user_info_dir"])) die("Username error");
    $user_record = get_user_record($username, $config['user_info_dir']);
    if($user_record->user->password != $password) die("Password error for User:".$user_record->user->username);
    header("Location:main.html");