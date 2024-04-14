## 张万森，下雪了

***

出题人：D0UBL3SEV3N

![image-20240413231003706](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413231003706.png)

考点：SNOW 隐写，字典爆破，base64 多次编码

解题步骤： 下载附件后得到一个压缩包和一个字典文件 dic.txt。压缩包里 面的 txt 文件需要密码，dic.txt 爆破压缩包密码。使用 ARCHPR.exe 字典文件破解密码。

得到压缩包里面的文件密码：blueSHARK666

tip.txt 里的密文是经过 base64 进行 17次编码后得到的，对这 段密文进行 17 次 base64 解密，脚本如下：

```python
import base64
Sstr=''
with open('tip.txt', 'r', encoding='UTF-8') as f: #打开 tip.txt 文件
 Sstr="".join(f.readlines()).encode('utf-8')
src=Sstr
while True: 
 try:
 src=Sstr
 Sstr=base64.b64decode(Sstr) #解码
 str(Sstr,'utf-8')
 continue
 except:
 pass
 break
with open('result.txt','w', encoding='utf-8') as file: #写入明文
 file.write(str(src,'utf-8'))
print('ok')

```

得到一些无法解密的字符，使用词频统计：

```python
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}[]"
# filename = input('请输入目标文本:')
data = input()
result = {d:0 for d in alphabet}#生成字典


def sort_by_value(d):
    items = d.items()
    backitems = [[v[1],v[0]] for v in items]
    backitems.sort(reverse=True)
    print(backitems,'\n\n') #按出现次数从大到小输出对应次数和字符
    return [ backitems[i][1] for i in range(0,len(backitems))]#按出现次数从大到小返回字符

for d in data:
    for alpha in alphabet:
        if d == alpha:
            result[alpha] = result[alpha] + 1 #字符出现一次加一

print(''.join(sort_by_value(result))) #连接成字符串


```

统计完成之后：

![descript](C:/Users/26272/Pictures/media/0524c0d4948dfa210c923628f2088c85.png)

查看 flag.txt，可以看到有信息被隐藏起来了，不难发现这是 SNOW 隐写，这里的 flag 是迷惑人的，真正的 flag 藏匿在 flag.txt 文件中。解密的密文就是刚刚得到的 ISCTFZ023。

解密如下：

```
SNOW.EXE -C -p "ISCTFZ023" flag.txt
```

这样才能得到真正的flag

![descript](C:/Users/26272/Pictures/media/7ee77b6722bd827bca31c6ffa2c6c12a.png)

