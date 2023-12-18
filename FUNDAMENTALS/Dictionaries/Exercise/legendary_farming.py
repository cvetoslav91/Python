dictionary = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
flag = False
while True:
    if flag:
        break
    materials = input().split()
    for i in range(0, len(materials), 2):
        key = materials[i + 1].lower()
        value = int(materials[i])
        if key in dictionary:
            dictionary[key] += value
        else:
            dictionary[key] = value
        if dictionary['shards'] >= 250:
            dictionary['shards'] -= 250
            print("Shadowmourne obtained!")
            flag = True
            break
        elif dictionary['fragments'] >= 250:
            dictionary['fragments'] -= 250
            print("Valanyr obtained!")
            flag = True
            break
        elif dictionary['motes'] >= 250:
            dictionary['motes'] -= 250
            print("Dragonwrath obtained!")
            flag = True
            break

for key, value in dictionary.items():
    print(f'{key}: {value}')