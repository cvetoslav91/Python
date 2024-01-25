from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        operator = symbols.popleft()
        if operator == '+':
            total_honey += abs(current_bee + current_nectar)
        elif operator == '-':
            total_honey += abs(current_bee - current_nectar)
        elif operator == '*':
            total_honey += abs(current_bee * current_nectar)
        elif operator == '/':
            if current_nectar == 0:
                continue
            total_honey += abs(current_bee / current_nectar)
    else:
        bees.appendleft(current_bee)

print(f'Total honey made: {total_honey}')
if bees:
    print("Bees left: ", end="")
    print(*bees, sep=', ')
elif nectar:
    print('Nectar left: ', end='')
    print(*nectar, sep=', ')