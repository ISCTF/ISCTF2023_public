from PIL import Image

#该脚本的目的是将图片3.png的像素提取出来，并添加到1.jpeg中
im1 = Image.open("1.jpeg")
im2 = Image.open("3.png")
print(im1.size)
print(im1.mode)
print(im2.size)
width_1 = im1.width   #获取图一宽高
height_1 = im1.height

width_2 = im2.width   #获取图二宽高
height_2 = im2.height

new_img1 = Image.new("RGB",(width_1,height_1))
new_img2 = Image.new("RGB",(width_2,height_2))

for x in range(width_1):
    for y in range(height_1):
        w1 = im1.getpixel((x,y))
        if x%10==0 and y%10==0:
            w2 = im2.getpixel((x//10,y//10))
            new_img1.putpixel((x,y),w2)
        else:
            new_img1.putpixel((x,y),w1)

new_img1.show()
new_img1.save("1new.png")




