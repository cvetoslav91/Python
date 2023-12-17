dictionary = {}
counter = 0
while True:
    command = input()
    if command == 'stop':
        break
    if counter % 2 == 0:
        key = command
    elif counter % 2 == 1:
        if key not in dictionary:
            dictionary[key] = int(command)
        else:
            dictionary[key] += int(command)
    counter += 1
for key, value in dictionary.items():
    print(f'{key} -> {value}')