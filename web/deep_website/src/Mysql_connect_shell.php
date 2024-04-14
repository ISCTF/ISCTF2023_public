<?php
require_once "config.php";

if(isset($_POST["sql"])){
	$sql = trim($_POST["sql"]);
	var_dump(fetchOne($sql));
}
else{
	highlight_file(__FILE__);
}

?>
