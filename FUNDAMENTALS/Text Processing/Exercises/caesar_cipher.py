word = input()
for char in word:
    result = ord(char) + 3
    new_char = chr(result)
    print(new_char, end='')