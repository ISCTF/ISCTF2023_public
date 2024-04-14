<?php
    include "utils/function.php";
    $config = include "utils/config.php";
    $user_xml_format = "<?xml version='1.0'?>
                        <userinfo>
                            <user>
                                <username>%s</username>
                                <password>%s</password>
                            </user>
                        </userinfo>";
    extract($_REQUEST);
    if(empty($username)||empty($password)) die("Username or password cannot be empty XD");

    if(!preg_match('/^[a-zA-Z0-9_]+$/', $username)) die("Invalid username. :(");

    if(is_user_exists($username, $config["user_info_dir"])) die("User already exists XD");
    $user_xml = sprintf($user_xml_format, $username, $password);

    register_user($username, $config['user_info_dir'], $user_xml);
