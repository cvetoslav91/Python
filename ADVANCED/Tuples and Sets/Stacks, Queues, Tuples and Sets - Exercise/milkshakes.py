from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milks = deque(int(x) for x in input().split(', '))
cups = 0

while cups < 5 and chocolates and milks:
    current_chocolate = chocolates.pop()
    current_milk = milks.popleft()
    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        milks.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    if current_chocolate == current_milk:
        cups += 1
    else:
        milks.append(current_milk)
        chocolates.append(current_chocolate - 5)

if cups == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")

if chocolates:
    print('Chocolate: ', end='')
    print(', '.join(map(str, chocolates)))
else:
    print('Chocolate: empty')

if milks:
    print('Milk: ',end='')
    print(', '.join(map(str, milks)))
else:
    print("Milk: empty")