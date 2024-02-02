from collections import deque

worms = [int(x) for x in input().split()]
all_worms = len(worms)
holes = deque(int(x) for x in input().split())
matches = 0
while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()
    if worm == hole:
        matches += 1
    elif worm != hole:
        worms.append(worm - 3)
    if worms:
        if worms[-1] <= 0:
            worms.pop()

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if matches == all_worms:
        print(f'Every worm found a suitable hole!')
    else:
        print("Worms left: none")
else:
    print(f'Worms left:',', '.join(str(x) for x in worms))

if not holes:
    print('Holes left: none')
else:
    print("Holes left:", ', '.join(str(x) for x in holes))