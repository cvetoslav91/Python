energy = int(input())
counter = 0
wins = 0
not_enough_energy = False
while True:
    distance = input()
    if distance == "End of battle":
        break
    distance = int(distance)
    if energy < distance:
        not_enough_energy = True
        break
    energy -= distance
    counter += 1
    wins += 1
    if counter == 3:
        energy += wins
        counter = 0

if not_enough_energy:
    print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
else:
    print(f"Won battles: {wins}. Energy left: {energy}")