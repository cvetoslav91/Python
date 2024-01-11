lines = int(input())
dictionary = {}
for i in range(lines):
    plant, rarity = input().split('<->')
    dictionary[plant] = {'Rarity': rarity, 'Rating': []}

while True:
    command = input()
    if command == 'Exhibition':
        break
    elif 'Rate' in command:
        rate, info = command.split(':')
        name, rating = info.split(' - ')
        name = name.strip()
        rating = int(rating)
        if name in dictionary:
            dictionary[name]['Rating'].append(rating)
        else:
            print('error')
    elif 'Update' in command:
        update, info = command.split(':')
        name, rarity = info.split(' - ')
        name = name.strip()
        if name in dictionary:
            dictionary[name]['Rarity'] = rarity
        else:
            print('error')
    elif 'Reset' in command:
        reset, name = command.split(':')
        name = name.strip()
        if name in dictionary:
            dictionary[name]['Rating'].clear()
        else:
            print('error')

print('Plants for the exhibition:')
for name, info in dictionary.items():
    lenght = len(dictionary[name]['Rating'])
    total_sum = sum(dictionary[name]['Rating'])
    if lenght > 0:
        average = total_sum / lenght
    else:
        average = 0
    print(f'- {name}; Rarity: {dictionary[name]["Rarity"]}; Rating: {average:.2f}')