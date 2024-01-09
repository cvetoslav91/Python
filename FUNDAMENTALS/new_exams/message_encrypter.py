import re

lines = int(input())
pattern = r'(\*|\@)([A-Z][a-z]{2,})(\1): \[([a-zA-Z])\]\|\[([a-zA-Z])\]\|\[([a-zA-Z])\]\|(?!.)'
for _ in range(lines):
    line = input()
    result = re.findall(pattern, line)
    if result:
        for i in result:
            tag = i[1]
            first_letter, second_letter, third_letter = i[3], i[4], i[5]
            print(f'{tag}: {ord(first_letter)} {ord(second_letter)} {ord(third_letter)}')
    else:
        print("Valid message not found!")