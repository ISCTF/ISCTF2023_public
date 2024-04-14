import qrcode
import random
import string
import os

def generate_random_string(length):
    # 生成指定长度的随机字符串
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def generate_qrcode(content):
    # 创建 QRCode 对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 添加数据到 QRCode 对象
    qr.add_data(content)
    qr.make(fit=True)

    # 创建 Image 对象
    img = qr.make_image(fill_color="black", back_color="white")

    # 调整图片大小为 256x256
    img = img.resize((256, 256))

    convert_image_to_mixed_numbers(img,'/task/flag.txt')

    # 保存二维码图片
    # img.save("isctf_qrcode.png")


def convert_image_to_mixed_numbers(img, output_file):
    # 打开图像
    # img = Image.open(image_path)

    # 转换为灰度图像
    img = img.convert("L")

    # 获取图像的大小
    width, height = img.size

    # 创建一个空的字符串来存储随机数
    mixed_numbers = ""

    # 遍历每个像素
    for y in range(height):
        for x in range(width):
            # 获取像素的颜色值
            pixel_color = img.getpixel((x, y))

            # 判断颜色是白色还是黑色，并添加相应的随机数到字符串
            if pixel_color == 255:  # 白色
                mixed_numbers += str(random.choice([0, 1, 2, 3, 9]))
            else:  # 黑色
                mixed_numbers += str(random.choice([4, 5 ,6 ,7 ,8]))

        # 在每行结束时添加换行符
        mixed_numbers += "\n"

    # 将随机数写入到txt文件
    with open(output_file, "w") as file:
        file.write(mixed_numbers)




if __name__ == "__main__":
    FLAG = str(os.getenv("FLAG"))
    os.putenv("FLAG","flag")
    generate_qrcode(FLAG)

