from collections import deque

quantity_of_food = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))
for i in range(len(orders)):
    if orders[0] <= quantity_of_food:
        quantity_of_food -= orders.popleft()
    else:
        print(f'Orders left: ', end='')
        for left in orders:
            print(left, end=' ')
        break

if not orders:
    print('Orders complete')
