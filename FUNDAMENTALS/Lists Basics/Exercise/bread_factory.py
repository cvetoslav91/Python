event = input().split('|')
energy = 100
coins = 100
forced_end = False
for current_event in event:
    separated_item = current_event.split('-')
    command = separated_item[0]
    value = int(separated_item[1])
    if command == 'rest':
        if energy + value > 100:
            value = 100 - energy
            energy = 100
        else:
            energy += value
        print(f'You gained {value} energy.')
        print(f"Current energy: {energy}.")
    elif command == 'order':
        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            forced_end = True
            break
if forced_end:
    pass
else:
    print('Day completed!')
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")