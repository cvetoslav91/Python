import re

text = input()

pattern = r'\b(_)([a-zA-Z0-9]+)\b'

result = re.finditer(pattern, text)
final_list = []
for i in result:
    to_add = i.group(2)
    final_list.append(to_add)

print(','.join(final_list))