import re

text = input()

while text:
    result = re.findall(r'\d+', text)
    if result:
        print(' '.join(result), end=" ")
    text = input()