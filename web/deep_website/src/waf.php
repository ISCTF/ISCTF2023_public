<?php

$black_list = ["/**/union","union/**/","/**/select","select/**/","union/**/select","load_file","insert"," ","limit","sleep","substr","left","right","and","xml",">","<","=","&&","||"];

function waf($string){
	global $black_list;
	$flag = False;
	$temp = $string;
	foreach ($black_list as $key => $value) {
		if(False !== stripos($string, $value)){
			$string = str_ireplace($value, "", $string);
			$flag = True;
		}
	}
	if($flag){
		return waf($string);
	}
	else{
		return $string;
	}

}

// var_dump(waf("select you OoRr hack"));
?>
