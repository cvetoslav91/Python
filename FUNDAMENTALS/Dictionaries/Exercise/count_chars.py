chars = [x for x in input()]
while ' ' in chars:
    chars.remove(' ')
dictionary = {}
for char in chars:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1
for key, value in dictionary.items():
    print(f'{key} -> {value}')