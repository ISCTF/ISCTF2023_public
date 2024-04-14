import base64
Sstr=''
with open('tip.txt', 'r', encoding='UTF-8') as f:
    Sstr="".join(f.readlines()).encode('utf-8')
src=Sstr
while True:
    try:
        src=Sstr
        Sstr=base64.b64decode(Sstr)
        str(Sstr,'utf-8')
        continue
    except:
        pass
    break
with open('result.txt','w', encoding='utf-8') as file:
    file.write(str(src,'utf-8'))
print('ok')

