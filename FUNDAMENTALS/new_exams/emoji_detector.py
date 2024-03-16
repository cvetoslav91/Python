import re
from functools import reduce

text = input()

regex = r'(:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)'
matches = re.findall(regex, text)

numbers = re.findall(r'\d', text)

if numbers:
    cool_threshhold = reduce(lambda x, y: x * y, map(int, numbers))
else:
    cool_threshhold = 0

cool_words = []
for match in matches:
    word_count = sum(ord(x) for x in list(match[1]))
    if word_count > cool_threshhold:
        cool_words.append(match)

print(f"Cool threshold: {cool_threshhold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for word in cool_words:
    print(''.join(word))