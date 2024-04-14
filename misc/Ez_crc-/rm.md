## Ez_crc

***

出题人：Dr34m

![image-20240413230259864](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413230259864.png)

<https://github.com/Dr34nn/CRC_Cracker>

```python
dictionary = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖','0': '零', 'a': '啊', 'b': '玻', 'c': '雌', 'd': '得', 'e': '鹅', 'f': '佛', 'g': '哥', 'h': '喝', 'i': '爱', 'j': '基','k': '科','l': '勒', 'm': '摸', 'n': '讷', 'o': '喔', 'p': '坡', 'q': '欺', 'r': '日', 's': '思', 't': '特','u': '乌','v': '迂','w': '巫', 'x': '希', 'y': '歪', 'z': '资'}
big = '大写的'
flag='output'
flipped_dict = {v: k for k, v in dictionary.items()}
i=0
while i < len(flag):
    if flag[i] in flipped_dict:
        print(flipped_dict[flag[i]],end='')
    else:
        i += 3
        print(flipped_dict[flag[i]].upper(),end='')
    i += 1

```

另一种写脚本爆破的方法

![descript](C:/Users/26272/Pictures/media/c293f405b3cc9f6675bc1860822808ac.png)

