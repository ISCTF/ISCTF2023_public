from PIL import Image

def convert_txt_to_image(input_file, output_image):
    with open(input_file, 'r') as file:
        content = file.read().strip().split('\n')

    # 计算图像大小
    width = len(content[0])
    height = len(content)

    # 创建图像对象
    img = Image.new('1', (width, height), color=0)

    # 设置像素值
    for y in range(height):
        for x in range(width):
            pixel_value = int(content[y][x])
            img.putpixel((x, y), pixel_value)

    # 保存图像为PNG文件
    img.save(output_image)

if __name__ == "__main__":
    input_file = "output.txt"  # 替换为你的输入文件路径
    output_image = "output.png"  # 替换为你的输出图像路径

    convert_txt_to_image(input_file, output_image)
    print(f"转换完成，结果保存在 {output_image}")
