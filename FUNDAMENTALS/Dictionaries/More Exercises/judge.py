import copy

def sorting(items):
    name, points = items
    return -points, name


stats = {}
while True:
    info = input()
    if info == "no more time":
        break
    name, course, points = info.split(' -> ')
    points = int(points)
    if course not in stats:
        stats[course] = {}
    copy_stats = copy.deepcopy(stats)
    for key, value in copy_stats.items():
        if name not in stats[course]:
            result = {name: points}
            stats[course].update(result)
        else:
            if stats[course][name] < points:
                stats[course][name] = points

for key, value in stats.items():
    sorted_values = dict(sorted(value.items(), key=sorting))
    stats[key] = sorted_values
final_standings = {}
for current_value in stats.values():
    for current_name, current_points in current_value.items():
        if current_name not in final_standings:
            final_standings[current_name] = current_points
        else:
            final_standings[current_name] += current_points

sorted_dictionary = dict(sorted(final_standings.items(), key=sorting))

for key, value in stats.items():
    print(f'{key}: {len(stats[key])} participants')
    n = 1
    for name, points in value.items():
        print(f'{n}. {name} <::> {points}')
        n += 1

print('Individual standings: ')
i = 1
for key, value in sorted_dictionary.items():
    print(f'{i}. {key} -> {value}')
    i += 1

