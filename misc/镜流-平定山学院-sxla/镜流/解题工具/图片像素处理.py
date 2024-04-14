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
