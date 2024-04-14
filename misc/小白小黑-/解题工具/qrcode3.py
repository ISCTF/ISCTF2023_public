def replace_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # 替换数字
    content = content.replace('0', '1').replace('1', '1').replace('2', '1').replace('3', '1').replace('9', '1')
    content = content.replace('4', '0').replace('5', '0').replace('6', '0').replace('7', '0').replace('8', '0')

    with open(output_file, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file = "isctf.txt"  # 替换为你的输入文件路径
    output_file = "output.txt"  # 替换为你的输出文件路径

    replace_numbers(input_file, output_file)
    print(f"替换完成，结果保存在 {output_file}")
