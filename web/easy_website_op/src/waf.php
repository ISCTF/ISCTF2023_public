<?php

$black_list = ["select","union","or","and"," "];

function waf($string){
	global $black_list;
	$temp = $string;
	foreach ($black_list as $key => $value) {
		if(False !== stripos($string, $value)){
			$string = str_ireplace($value, "", $string);
		}
	}
	return $string;
}

// var_dump(waf("select you OoRr hack"));
?>
