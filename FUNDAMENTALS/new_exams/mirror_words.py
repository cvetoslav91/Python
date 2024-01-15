import re

string = input()

pattern = r'([@|#])([a-zA-Z]{3,})(\1){2}([a-zA-Z]{3,})(\1)'
matches = {}
result = re.findall(pattern, string)
if result:
    print(f"{len(result)} word pairs found!")
    for match in result:
        first_word = match[1]
        second_word = match[3]
        if first_word == second_word[-1::-1]:
            matches[first_word] = second_word
else:
    print("No word pairs found!")
if matches:
    print(f"The mirror words are:")
    output = ', '.join(f'{key} <=> {value}' for key, value in matches.items())
    print(output)
else:
    print("No mirror words!")
