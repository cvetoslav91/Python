from collections import deque

fuel = deque([int(x) for x in input().split()])
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])
reached_alts = []

for alt in range(1, 5):
    current_fuel = fuel.pop()
    consumed_fuel = consumption.popleft()
    current_need = needed_fuel.popleft()
    difference = current_fuel - consumed_fuel

    if difference >= current_need:
        print(f'John has reached: Altitude {alt}')
        reached_alts.append(f'Altitude {alt}')
    else:
        print(f'John did not reach: Altitude {alt}')
        break
else:
    print("John has reached all the altitudes and managed to reach the top!")
    exit()

print('John failed to reach the top.')
if not reached_alts:
    print("John didn't reach any altitude.")
else:
    print('Reached altitudes:', ", ".join(reached_alts))