<?php
error_reporting(0);

if ($_FILES['file']['error'] > 0) {
    die("文件传输失败");
}
$file = $_FILES['file'];
if (isset($file) && $file['size'] > 0) {
    $ext = end(explode(".", $file['name']));
    $name = substr($file['name'], 0, stripos($file['name'], $ext));
    if (preg_match("/ph|jsp|jtml|as|cer|swf|htaccess/i", $ext)) {
        die("你这文件类型不太行啊");
    }
    if (preg_match('/</i',file_get_contents($file['tmp_name']))) {
        die("就你还想在我面前传马？");
    }
    
    $dis_name = $name . $ext;
    if (move_uploaded_file($file['tmp_name'], './' . $dis_name)) {
        echo "文件上传成功，文件上传路径为：" . './' . $dis_name;
    } else {
        echo "文件上传失败，未知原因......";
    }
    die();
}
?>
