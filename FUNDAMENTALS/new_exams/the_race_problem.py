import re

line = input()
pattern = r'([\#\$\%\*\&])([A-Za-z]+)\1=(\d+)!!(.+)'
while line:
    result = re.search(pattern, line)
    if result:
        if len(result.group(4)) == int(result.group(3)):
            help_list = []
            for char in result.group(4):
                new_char = chr(ord(char) + int(result.group(3)))
                help_list.append(new_char)
                final = ''.join(help_list)
            print(f'Coordinates found! {result.group(2)} -> {final}')
            break
        else:
            print('Nothing found!')
    else:
        print(f'Nothing found!')
    line = input()