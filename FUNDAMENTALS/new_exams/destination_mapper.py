import re

string = input()

pattern = r'(\=|\/)([A-Z][a-zA-Z]{2,})(\1)'

result = re.findall(pattern, string)
destination = []
total_points = 0
for i in result:
    destination.append(i[1])
    total_points += len(i[1])
print('Destinations:', end=' ')
print(', '.join(destination))
print(f'Travel Points: {total_points}')