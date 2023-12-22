import copy
dwarfs = {}
while True:
    info = input()
    if info == 'Once upon a time':
        break
    name, hat_color, physics = info.split(' <:> ')
    physics = int(physics)
    if hat_color not in dwarfs:
        dwarfs[hat_color] = {name: physics}
    else:
        if name not in dwarfs[hat_color]:
            dwarfs[hat_color][name] = physics
        else:
            if physics > dwarfs[hat_color][name]:
                dwarfs[hat_color][name] = physics
final = {}
max_value = 0
new = {}

final = dict(sorted(dwarfs.items(), key=lambda x: len(x[1]), reverse=True))
for key, value in final.items():
    sorted_values = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    new[key] = sorted_values

while True:
    if not new:
        break
    new_copy = copy.deepcopy(new)
    for color, name_pts in new_copy.items():
        max_value = max(value for inner_dict in new_copy.values() for value in inner_dict.values())
        for name, points in name_pts.items():
            if points == max_value:
                print(f'({color}) {name} <-> {points}')
                del new[color][name]
                if not new[color]:
                    del new[color]