rooms = input().split('|')
current_health = 100
bitcoins = 0
died = False
for current_room in range(1, len(rooms) + 1):
    command = rooms[current_room - 1]
    command_list = command.split()
    monster = command_list[0]
    value = int(command_list[1])
    if monster == 'potion':
        if current_health + value > 100:
            value = 100 - current_health
        current_health += value
        print(f"You healed for {value} hp.")
        print(f'Current health: {current_health} hp.')
    elif monster == 'chest':
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        current_health -= value
        if current_health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {current_room}")
            died = True
            break
        else:
            print(f"You slayed {monster}.")
if not died:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {current_health}')
