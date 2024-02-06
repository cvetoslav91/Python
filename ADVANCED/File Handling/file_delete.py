import os.path

path = os.path.join('files', 'my_first_file')

try:
    os.remove(path)
except FileNotFoundError:
    print('File already deleted')