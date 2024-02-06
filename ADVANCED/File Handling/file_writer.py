import os.path

path = os.path.join('files', 'my_first_file')

with open(path, 'w') as file:
    file.write('I just created my first file')