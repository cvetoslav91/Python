import re

demons = re.split(", *", input())
dictionary = {}
for current_demon in demons:
    damage = 0
    pattern = r'[^\+\-\*\/\.\d]'
    result = re.findall(pattern, current_demon)
    numbers = [ord(x) for x in result]
    health = sum(numbers)
    pattern_for_damage = r'((\+|\-)?[0-9]+(\.\d*)?)'
    new_result = re.findall(pattern_for_damage, current_demon)
    for i in new_result:
        damage += float(i[0])
    stars_and_slashes = re.findall(r'[\/\*]', current_demon)
    for current_sign in stars_and_slashes:
        if current_sign == '/':
            damage /= 2
        elif current_sign == '*':
            damage *= 2
    dictionary[current_demon] = [health, damage]

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
for name, info in sorted_dictionary.items():
    print(f'{name} - {info[0]} health, {info[1]:.2f} damage')
