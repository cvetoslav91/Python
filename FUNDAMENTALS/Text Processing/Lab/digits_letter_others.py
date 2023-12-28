word = input()
digits = ''
letters = ''
others = ''
for char in word:
    if char.isnumeric():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(digits)
print(letters)
print(others)