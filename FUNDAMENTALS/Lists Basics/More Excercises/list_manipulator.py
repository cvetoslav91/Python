list = input().split()
command = input()
even_list = []
odd_list = []
for i in range(len(list)):
    list[i] = int(list[i])
for current_number in list:
    if current_number % 2 == 0:
        even_list.append(current_number)
    else:
        odd_list.append(current_number)
while command != 'end':
    command_as_list = command.split()
    first_even_list = []
    first_odd_list = []
    last_even_list = []
    last_odd_list = []
    if command_as_list[0] == 'exchange':
        value = int(command_as_list[1])
        if value >= len(list) or value < 0:
            print('Invalid index')
            command = input()
            continue
        first_part = list[value + 1:]
        second_part = list[:value + 1]
        list = first_part + second_part
    elif command_as_list[0] == 'max' or command_as_list[0] == 'min':
        if command_as_list[0] == 'max':
            if command_as_list[1] == 'even' and len(even_list) != 0:
                max_number = max(even_list)
                for i in range(len(list)):
                    if list[i] == max_number:
                        index = i
                print(index)
            elif command_as_list[1] == 'odd' and len(odd_list) != 0:
                max_number = max(odd_list)
                for i in range(len(list)):
                    if list[i] == max_number:
                        index = i
                print(index)
            else:
                print('No matches')
        elif command_as_list[0] == 'min':
            if command_as_list[1] == 'even' and len(even_list) != 0:
                min_number = min(even_list)
                for i in range(len(list)):
                    if list[i] == min_number:
                        index = i
                print(index)
            elif command_as_list[1] == 'odd' and len(odd_list) != 0:
                min_number = min(odd_list)
                for i in range(len(list)):
                    if list[i] == min_number:
                        index = i
                print(index)
            else:
                print('No matches')
    elif command_as_list[0] == 'first' or command_as_list[0] == 'last':
        if command_as_list[0] == 'first':
            if command_as_list[2] == 'even' and int(command_as_list[1]) <= len(list):
                for j in list:
                    if j % 2 == 0:
                        first_even_list.append(j)
                        if len(first_even_list) == int(command_as_list[1]):
                            break
                print(first_even_list)
            elif command_as_list[2] == 'odd' and int(command_as_list[1]) <= len(list):
                for j in list:
                    if j % 2 != 0:
                        first_odd_list.append(j)
                        if len(first_odd_list) == int(command_as_list[1]):
                            break
                print(first_odd_list)
            else:
                print("Invalid count")
        elif command_as_list[0] == 'last':
            if command_as_list[2] == 'even' and int(command_as_list[1]) <= len(list):
                for j in range(len(list) - 1, -1, -1):
                    if list[j] % 2 == 0:
                        last_even_list.insert(0, list[j])
                        if len(last_even_list) == int(command_as_list[1]):
                            break
                print(last_even_list)
            elif command_as_list[2] == 'odd' and int(command_as_list[1]) <= len(list):
                for j in range(len(list) - 1, -1, -1):
                    if list[j] % 2 != 0:
                        last_odd_list.insert(0, list[j])
                        if len(last_odd_list) == int(command_as_list[1]):
                            break
                print(last_odd_list)
            else:
                print("Invalid count")
    command = input()
print(list)





