my_list = []
while True:
    command = input()
    if command == 'End':
        break
    else:
        my_list.append(command)
        my_list.sort(key=lambda x: int(x.split('-')[0]))
result = [command.split('-')[1] for command in my_list]
print(result)