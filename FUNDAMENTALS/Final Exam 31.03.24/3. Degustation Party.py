guests = {}
unliked_meals = 0

while True:

    command = input().split('-')
    if command[0] == "Stop":
        break

    guest = command[1]
    meal = command[2]

    if command[0] == "Like":
        if guest not in guests:
            guests[guest] = []
        if meal not in guests[guest]:
            guests[guest].append(meal)

    elif command[0] == "Dislike":
        if guest in guests:
            if meal in guests[guest]:
                guests[guest].remove(meal)
                unliked_meals += 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")


for g, meals in guests.items():
    print(f"{g}: {', '.join(meals)}")

print(f'Unliked meals: {unliked_meals}')
