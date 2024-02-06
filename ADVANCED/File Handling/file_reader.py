import os.path

path = os.path.join('files', 'numbers.txt')
total = 0

with open(path) as file:
    for number in file.read():
        if number.isdigit():
            total += int(number)

print(total)