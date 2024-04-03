import re

regex = r'(!)([A-Z][a-z]{3,})(\1):\[([A-Za-z]{8,})\]'

n = int(input())

for _ in range(n):
    message = input()

    result = re.findall(regex, message)
    if result:
        command = result[0][1]
        string = result[0][3]
        print(f"{command}: {' '.join([str(ord(c)) for c in string])}")
    else:
        print('The message is invalid')
