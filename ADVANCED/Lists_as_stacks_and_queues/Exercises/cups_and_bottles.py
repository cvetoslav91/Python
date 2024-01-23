from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0
while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_bottle > current_cup:
        wasted_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)
        if cups[0] == 0:
            cups.popleft()

if cups:
    print('Cups: ',end='')
    print(' '.join(map(str, cups)))
elif bottles:
    print('Bottles: ',end='')
    print(' '.join(map(str, bottles)))

print(f'Wasted litters of water: {wasted_water}')