<?php
echo 'show me your parameter!!!';
$file=$_GET['mihoyo'];
if( isset($file) )
	include( $file );
else {
	echo 'Wrong parameter!!!';
}
?>
