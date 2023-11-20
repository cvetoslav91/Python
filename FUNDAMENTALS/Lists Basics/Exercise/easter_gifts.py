gifts = input()
my_list = gifts.split(' ')
command = input()
while command != 'No Money':
    list_command = command.split(' ')
    command = list_command[0]
    gift = list_command[1]
    if command == 'OutOfStock':
        while gift in my_list:
            index = my_list.index(gift)
            my_list[index] = 'None'
    elif command == 'Required':
        index = int(list_command[2])
        if 0 <= index < len(my_list):
            my_list[index] = gift
    elif command == 'JustInCase':
        my_list[-1] = gift
    command = input()
while 'None' in my_list:
    my_list.remove('None')
for k in my_list:
    print(k, end =' ')