#!/bin/sh

if [ "$DASFLAG" ]; then
    INSERT_FLAG="$DASFLAG"
elif [ "$FLAG" ]; then
    INSERT_FLAG="$FLAG"
elif [ "$GZCTF_FLAG" ]; then
    INSERT_FLAG="$GZCTF_FLAG"
else
    INSERT_FLAG="ISCTF{Fuzz_is_a_great_trick_Did_you_find_curly_braces?-Jay17}"
fi

# 将FLAG写入文件 请根据需要修改
#echo $INSERT_FLAG | tee /home/$user/flag /flag
echo 'ISCTF{Fuzz_is_a_great_trick_Did_you_find_curly_braces?-Jay17}' > /flaggggggg.txt
