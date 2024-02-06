import os.path
import re

words_open_path = os.path.join('files', 'words.txt')
input_path = os.path.join('files', 'input.txt')

dictionary = {}

with open(words_open_path) as file:
    words = file.read()
    searched_words = [x.lower() for x in words.split()]

with open(input_path) as file:
    content = file.read().lower()

for word in searched_words:
    result = re.findall(rf'\b{word}\b', content)
    dictionary[word] = len(result)

result = sorted(dictionary.items(), key=lambda x: -x[1])
new_file_path = os.path.join('files', 'output.txt')
with open(new_file_path, 'a') as file:
    for word, value in result:
        file.write(f'{word} - {value}\n')

