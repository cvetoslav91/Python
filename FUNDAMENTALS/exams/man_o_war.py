pirate_ship = [int(s) for s in input().split('>')]
warship = [int(s) for s in input().split('>')]
max_health = int(input())
win = False
while True:
    if win:
        break
    command = input().split()
    if command[0] == 'Retire':
        print(f'Pirate ship status: {sum(pirate_ship)}')
        print(f'Warship status: {sum(warship)}')
        break
    elif command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if index < 0 or index > len(warship) - 1:
            continue
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            win = True
            break
    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index < 0 or end_index > len(pirate_ship) - 1:
            continue
        for part in range(start_index, end_index + 1):
            pirate_ship[part] -= damage
            if pirate_ship[part] <= 0:
                print("You lost! The pirate ship has sunken.")
                win = True
                break
    elif command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if index < 0 or index > len(pirate_ship) - 1:
            continue
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health
    elif command[0] == 'Status':
        parts_need_repair = [s for s in pirate_ship if s < max_health * 0.2]
        print(f"{len(parts_need_repair)} sections need repair.")
