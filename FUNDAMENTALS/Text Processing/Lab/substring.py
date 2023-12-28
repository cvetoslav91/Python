string = input()
substring = input()
while string in substring:
    substring = substring.replace(string, "")
print(substring)