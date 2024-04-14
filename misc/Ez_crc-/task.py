# -*- coding: utf-8 -*-
import base64
import os
import uuid
flag = str(os.getenv("FLAG")).encode()
os.putenv("FLAG",'flag')
os.environ['FLAG']='flag'
flag = base64.b64encode(flag)
flag = base64.b64encode(flag).decode()
dictionary = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖',
              '0': '零'
    , 'a': '啊', 'b': '玻', 'c': '雌', 'd': '得', 'e': '鹅', 'f': '佛', 'g': '哥', 'h': '喝', 'i': '爱', 'j': '基',
              'k': '科',
              'l': '勒', 'm': '摸', 'n': '讷', 'o': '喔', 'p': '坡', 'q': '欺', 'r': '日', 's': '思', 't': '特',
              'u': '乌',
              'v': '迂',
              'w': '巫', 'x': '希', 'y': '歪', 'z': '资', '+': '加', '/': '斜', '=': '等'}
big = '大写的'
output = ''
for i in flag:
    if i in dictionary:
        output += dictionary[i]
    elif i.lower() in dictionary:
        output += big + dictionary[i.lower()]
for i in range(len(output)):
    with open('./task/'+str(i) +'.txt','a',encoding='utf-8') as f:
        f.write(output[i])
    f.close()
pwd=str(uuid.uuid4())
os.system('zip -q -r -j -P '+pwd+' /flag.zip /task/*.txt')

