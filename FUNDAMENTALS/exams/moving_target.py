def shoot(targets, index, power):
    if index < 0 or index >= len(targets):
        return targets
    targets[index] -= power
    if targets[index] <= 0:
        targets.pop(index)
    return targets


def add(targets, index, value):
    if index < 0 or index >= len(targets):
        print("Invalid placement!")
        return targets
    targets.insert(index, value)
    return targets


def strike(targets, index, radius):
    if index - radius < 0 or index + radius >= len(targets):
        print("Strike missed!")
        return targets
    new_list_first_half = targets[:index - radius]
    new_list_second_half = targets[index + radius + 1:]
    final_list = new_list_first_half + new_list_second_half
    return final_list

targets = [int(x) for x in input().split()]
while True:
    command = input().split()
    if command[0] == 'End':
        print('|'.join(map(str, targets)))
        break
    index = int(command[1])
    value = int(command[2])
    if command[0] == 'Shoot':
        targets = shoot(targets, index, value)
    elif command[0] == 'Add':
        targets = add(targets, index, value)
    elif command[0] == 'Strike':
        targets = strike(targets, index, value)


