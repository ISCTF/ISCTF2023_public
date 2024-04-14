from Crypto.Util.number import bytes_to_long

s = 'ID71QI6UV7NRV5ULVJDJ1PTVJDVINVBQUNT'

binary_str = ''
for char in s:
    if '0' <= char <= '9':
        value = int(char)
    else:  # A-E
        value = 10 + ord(char) - ord('A')
    binary_repr = bin(value)[2:].zfill(5)
    binary_str += binary_repr

# Convert the binary string to ASCII
decoded_str = ''
for i in range(0, len(binary_str), 7):
    char_value = int(binary_str[i:i+7], 2)
    decoded_str += chr(char_value)

print(decoded_str)
