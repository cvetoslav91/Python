import re
pattern = r'(www\.[a-zA-Z0-9\-]+\.[a-z]+(\.?[a-z]+)+)'
line = input()
while line:
    result = re.findall(pattern, line)
    if result:
        for current in result:
            print(current[0])
    line = input()