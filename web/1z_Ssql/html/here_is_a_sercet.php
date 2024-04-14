<?php
highlight_file("here_is_a_sercet.php");

function waf($str){
    $black_list = "762V08zk+xrmKxIFrdJIJj6ULvI8Lc0pX39LjDyIUb0eAGkZe4KQa87TJXuqnFw0u/669wWRsqYFya812FtULw9+tpiGlaH2gleDfDKzr+g=";
    if (preg_match($black_list,$str)){
        die("<h4>illegal words!</h4>");
    }
    return $str;
}

?>