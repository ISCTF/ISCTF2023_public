<?php



    function is_user_exists($username, $user_info_dir): bool
    {
        $dirs = array_filter(glob($user_info_dir . '/*'), 'is_dir');
        foreach ($dirs as $dir) {
            $dirName = basename($dir);
            if($dirName === $username) return true;

        }
        return false;
    }

    function register_user($username, $user_info_dir, $user_xml){
        $user_dir_name = $user_info_dir.$username;
        mkdir($user_dir_name, 0777);
        file_put_contents($user_dir_name.'/'.$username.".xml", $user_xml);
    }

    function get_user_record($username, $user_info_dir)
    {
        $user_info_xml = file_get_contents($user_info_dir.$username.'/'.$username.'.xml');
        $dom = new DOMDocument();
        $dom->loadXML($user_info_xml, LIBXML_NOENT | LIBXML_DTDLOAD);
        return simplexml_import_dom($dom);
    }
