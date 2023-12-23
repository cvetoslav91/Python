n = int(input())
dragons = {}
for current_dragon in range(n):
    color, name, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    damage, health, armor = int(damage), int(health), int(armor)
    if color not in dragons.keys():
        dragons[color] = {name: [damage, health, armor]}
    else:
        dragons[color][name] = [damage, health, armor]
new={}
for name, info in dragons.items():
    sorted_values = dict(sorted(info.items()))
    new[name] = sorted_values

help_dictionary = {}
for color, info in new.items():
    total_d, total_h, total_a = 0, 0, 0
    counter = 0
    for name, stats in info.items():
        d = stats[0]
        h = stats[1]
        a = stats[2]
        total_d += d
        total_h += h
        total_a += a
        counter += 1
    avg_d = (total_d / counter)
    avg_h = (total_h / counter)
    avg_a = (total_a / counter)
    avg_d = f'{avg_d:.2f}'
    avg_h = f'{avg_h:.2f}'
    avg_a = f'{avg_a:.2f}'
    help_dictionary[color] = [avg_d, avg_h, avg_a]

for color, avg_stats in help_dictionary.items():
    str_stats = [str(x) for x in avg_stats]
    result = '/'.join(str_stats)
    print(f'{color}::({result})')
    for dragon_color, dragon_info in new.items():
        if color == dragon_color:
            for name, stats in dragon_info.items():
                print(f'-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}')
