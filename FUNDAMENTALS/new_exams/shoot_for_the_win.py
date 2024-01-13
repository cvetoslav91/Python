targets = [int(x) for x in input().split()]
final_list = []
shots = 0
while True:
    command = input()
    if command == 'End':
        break
    index = int(command)
    if index >= len(targets):
        continue
    number = targets[index]
    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        elif targets[i] <= number:
            targets[i] += number
        else:
            targets[i] -= number
    targets[index] = -1
    shots += 1

print(f"Shot targets: {shots} -> ", end='')
print(' '.join(map(str, targets)))