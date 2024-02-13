from collections import deque

monsters = deque([int(x) for x in input().split(',')])
strikes = deque([int(x) for x in input().split(',')])

monsters_killed = 0

while monsters and strikes:
    current_monster = monsters.popleft()
    current_strike = strikes.pop()

    if current_strike >= current_monster:
        diff = current_strike - current_monster
        if strikes:
            strikes[-1] += diff
        elif diff > 0 and not strikes:
            strikes.append(diff)
        monsters_killed += 1
    elif current_monster > current_strike:
        diff = current_monster - current_strike
        monsters.append(diff)

if not monsters:
    print("All monsters have been killed!")
if not strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")



