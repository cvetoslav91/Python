import re

title_pattern = r'<title>(.+)<\/title>'
body_pattern = r'<body>.+<\/body>'
text_pattern = r'(?<=>)[^<>]+'

html = input()
title = re.findall(title_pattern, html)
body = re.findall(body_pattern, html)
for i in body:
    info = re.findall(text_pattern, i)
final_title = ''.join(title)
final_string = ' '.join(info)
without_n = final_string.replace('\\n', '')
final_replace = without_n.replace('  ', ' ')
print(f"Title: {final_title}")
print(f"Content: {final_replace}")