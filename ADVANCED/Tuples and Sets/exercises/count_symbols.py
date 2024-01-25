text = input()
chars = {}
for char in text:
    if char not in chars:
        chars[char] = 0
    chars[char] += 1

chars = dict(sorted(chars.items()))
for key, value in chars.items():
    print(f'{key}: {value} time/s')


