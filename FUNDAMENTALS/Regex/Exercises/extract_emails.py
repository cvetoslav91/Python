import re

text = input()

pattern = r'\s([a-z0-9]+[a-z0-9_\.\-]*@[a-z][a-z\-]+(\.[a-z]+)+)'

result = re.findall(pattern, text)
for mail in result:
    print(mail[0])