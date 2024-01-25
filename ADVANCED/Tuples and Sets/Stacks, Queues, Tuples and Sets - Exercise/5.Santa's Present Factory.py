from collections import deque

def toy(dict, value):
    for key,info in dict.items():
        if value == info[0]:
            return key


materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())
toys = {
    'Doll': [150, 0],
    'Wooden train': [250, 0],
    'Teddy bear': [300, 0],
    'Bicycle': [400, 0]
}

dolls, trains, bears, bicycles = 0, 0, 0, 0
made_it = False
while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    total_magic_level = current_material * current_magic

    new_toy = toy(toys, total_magic_level)
    if new_toy:
        toys[new_toy][1] += 1
        if toys['Doll'][1] >= 1 and toys['Wooden train'][1] >= 1:
            made_it = True
            continue
        if toys['Teddy bear'][1] >= 1 and toys['Bicycle'][1] >= 1:
            made_it = True
            continue
        continue


    if total_magic_level < 0:
        materials.append(current_material + current_magic)
    elif total_magic_level > 0:
        materials.append(current_material + 15)
    elif total_magic_level == 0:
        if current_material != 0:
            materials.append(current_material)
        if current_magic != 0:
            magic.appendleft(current_magic)

if made_it:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    print('Materials left: ', end='')
    for i in range(len(materials) - 1, -1, -1):
        if i == 0:
            print(materials[0])
        else:
            print(materials[i], end=', ')
if magic:
    print('Magic left: ',end="")
    print(*magic, sep=', ')
toys = dict(sorted(toys.items()))
for name, info in toys.items():
    if info[1] > 0:
        print(f'{name}: {info[1]}')