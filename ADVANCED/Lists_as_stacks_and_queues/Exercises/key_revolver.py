from collections import deque

price_of_bullet = int(input())
size_of_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = [int(x) for x in input().split()]
locks = locks[-1::-1]
intelligence = int(input())
current_bullets_in_the_barrel = size_of_barrel
money_spent = 0

while bullets and locks:
    current_lock = locks[-1]
    current_bullet = bullets.pop()
    if current_bullet <= current_lock:
        locks.pop()
        print('Bang!')
        money_spent += price_of_bullet
    else:
        print('Ping!')
        money_spent += price_of_bullet
    current_bullets_in_the_barrel -= 1
    if bullets:
        if current_bullets_in_the_barrel == 0:
            print('Reloading!')
            current_bullets_in_the_barrel = size_of_barrel

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${intelligence - money_spent}')
    exit()
if not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")