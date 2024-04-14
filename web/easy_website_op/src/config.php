<?php
$mysql_user = "root";
$mysql_pwd = "root";
$mysql_host = "localhost";

$con = mysqli_connect($mysql_host,$mysql_user,$mysql_pwd);
if(!$con)
{
    exit('数据库连接失败'.mysqli_connect_error());
}

$mysql_database = "users";
mysqli_select_db($con,$mysql_database);  //定义默认查询的数据库

function fetchOne($sql)
{
    global $con;
    $res = mysqli_query($con,$sql);
    if(!$res)
    {
        echo '数据库查询失败：'.mysqli_error($con);
    }
    $row = mysqli_fetch_array($res);
    return $row;
}

?>
