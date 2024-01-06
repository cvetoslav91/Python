import re

text = input()
substring = input()

# pattern = fr'(?i)\b{substring}\b'
# result = re.findall(pattern, text)

pattern = fr'\b{substring}\b'
result = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(result))