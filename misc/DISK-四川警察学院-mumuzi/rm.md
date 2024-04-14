## DISK

***

出题人：mumuzi

![image-20240413230136545](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413230136545.png)

winhex打开磁盘，找到\$Extend---\$UsnJrnl---\$J

导出，然后使用NTFS Log Tracker（当然这里内容很少可以手动分析不需要这个也可以的）

加载\$J文件，然后生成db文件，导出csv

能够发现有很多修改前和修改后的内容

这里修改前的数字.txt如下：

[1230193492,1182487903,1918846768,811884366,1413895007,1298230881,1734701693]

```python
from libnum import n2s
s = [1230193492,1182487903,1918846768,811884366,1413895007,1298230881,1734701693]
print(''.join(n2s(i).decode() for i in s))

```



