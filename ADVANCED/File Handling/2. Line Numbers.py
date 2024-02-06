import os.path
from string import punctuation

path = os.path.join('files', 'text.txt')

with open(path) as file:
    text = file.readlines()


for row in range(len(text)):
    letters, marks = 0, 0
    for char in text[row]:
        if char.isalpha():
            letters += 1
        elif char in punctuation:
            marks += 1

    print(f"Line {row + 1}: {text[row].strip()}({letters})({marks})")