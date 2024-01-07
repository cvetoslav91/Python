import re

names = input().split(', ')
dictionary = {}
for current_name in names:
    dictionary[current_name] = 0

while True:
    command = input()
    if command == 'end of race':
        break
    total_time_list = re.findall(r'\d', command)
    total_time_list_ints = [int(x) for x in total_time_list]
    total_time = sum(total_time_list_ints)
    name = re.sub(r'[^a-zA-Z]', '', command)
    if name in names:
        dictionary[name] += total_time

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
final = iter(sorted_dictionary)
first = next(iter(final))
second = next(iter(final))
third = next(iter(final))
print(f'1st place: {first}')
print(f'2nd place: {second}')
print(f'3rd place: {third}')

