import os.path

path = os.path.join('files', 'text.txt')

try:
    with open(path) as file:
        print('File found')
except FileNotFoundError:
    print('File not found')