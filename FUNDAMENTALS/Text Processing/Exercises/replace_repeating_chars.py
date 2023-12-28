string = input()
final_string = ''
last_char = ' '
for char in string:
    if char != last_char:
        print(char, end="")
        last_char = char