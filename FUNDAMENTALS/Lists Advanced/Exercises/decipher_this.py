def first_letter(word):
    word = list(word)
    digit_list = []
    letters_list = []
    for digit in word:
        if digit.isdigit():
            digit_list.append(digit)
        else:
            letters_list.append(digit)
    digit_list = ''.join(digit_list)
    letters_list[0], letters_list[-1] = letters_list[-1], letters_list[0]
    return int(digit_list), letters_list



words = input().split()
for current_word in words:
    number, string = first_letter(current_word)
    first_char = chr(number)
    second_char = ''.join(string)
    print(f'{first_char}{second_char}', end=" ")