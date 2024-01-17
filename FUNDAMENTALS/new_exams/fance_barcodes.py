import re

words = int(input())

pattern = r'@#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])@#{1,}'

for i in range(words):
    new_word = input()
    result = re.findall(pattern, new_word)
    if not result:
        print('Invalid barcode')
        continue
    new_string = ''.join(result)
    digits = []
    for char in new_string:
        if char.isdigit():
            digits.append(char)
    if digits:
        final_result = ''.join(digits)
        print(f'Product group: {final_result}')
    else:
        print('Product group: 00')