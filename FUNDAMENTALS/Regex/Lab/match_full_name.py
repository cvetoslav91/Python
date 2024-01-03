import re

name = input()

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
result = re.findall(pattern, name)
print(" ".join(result))