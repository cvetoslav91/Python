import os.path
import re

path = os.path.join('files', 'text.txt')

with open(path, 'r') as file:
    content = file.read()

char_to_remove = ["-", ",", ".", "!", "?"]
rows = content.split('\n')
for i in range(len(rows)):
    if i % 2 == 0:
        result = re.sub(r'\-|,|\.|!|\?', "@", rows[i])
        list = result.split()
        print(*list[-1::-1])