text = input().split()
total_sum = 0
for current_word in text:
    first_letter = current_word[0]
    last_letter = current_word[-1]
    number = int(current_word[1:-1])
    if first_letter.isupper():
        result = number / (ord(first_letter) - 64)
    else:
        result = number * (ord(first_letter.upper()) - 64)
    if last_letter.isupper():
        result -= ord(last_letter) - 64
    else:
        result += ord(last_letter.upper()) - 64
    total_sum += result
print(f'{total_sum:.2f}')