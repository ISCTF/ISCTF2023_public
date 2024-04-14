## 镜流

***

出题人：sxla

压缩包是6位数字密码，需要使用ARCHPR进行6位数字爆破，密码是306256

压缩包解压出来是一张图片和一个提示文件，缩小10倍的意思是，图片中的像素点的间距是10，按照这个原理可以提取像素点合成另一张图片。

下面提供python脚本：

```python
from PIL import Image
#该脚本的目的是将1new.png中隐藏的图片提取出来
im1 = Image.open("1new.png")

width = im1.width//10
height = im1.height//10

new = Image.new("RGB",(width,height))
for x in range(width):
    for y in range(height):
        w1 = im1.getpixel((x*10,y*10))
        new.putpixel((x,y),w1)
new.show()
new.save("flag.png")

```

提取的图片使用zsteg可以提取出有flag的图片。



