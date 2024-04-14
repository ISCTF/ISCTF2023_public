## mfx_re
***

出题人：f00001111

![image-20240413224149587](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224149587.png)

考点：UPX魔改壳

签到题，将附件中的MFX替换为UPX，mfx替换为upx，使用upx脱壳，使用IDA分析，得到程序逻辑为将输入的字符串中每个字符减1，并与程序内字符串进行对比，编写脚本还原即可。

```python
a="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
for i in a:
 print(chr(ord(i)-1),end='')

```