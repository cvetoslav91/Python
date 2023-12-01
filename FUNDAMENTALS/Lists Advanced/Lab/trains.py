trains_list = [0] * int(input())
while True:
    command = input().split()
    if command[0] == 'End':
        print(trains_list)
        break
    elif command[0] == 'add':
        trains_list[-1] += int(command[1])
    elif command[0] == 'insert':
        trains_list[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        trains_list[int(command[1])] -= int(command[2])
