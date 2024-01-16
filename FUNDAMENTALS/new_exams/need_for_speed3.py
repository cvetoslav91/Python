number_of_cars = int(input())
cars = {}
for i in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    if car not in cars:
        cars[car] = [int(mileage), int(fuel)]
while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break
    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        cars_copy = cars.copy()
        for current_car, info in cars_copy.items():
            if car == current_car:
                if info[1] < fuel:
                    print("Not enough fuel to make that ride")
                else:
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                    cars[current_car][0] += distance
                    cars[current_car][1] -= fuel
                    if cars[current_car][0] >= 100000:
                        print(f"Time to sell the {current_car}!")
                        del cars[current_car]
    elif command[0] == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        old_fuel = cars[car][1]
        cars[car][1] = old_fuel + fuel
        if cars[car][1] > 75:
            cars[car][1] = 75
        difference = cars[car][1] - old_fuel
        print(f"{car} refueled with {difference} liters")

    elif command[0] == 'Revert':
        car = command[1]
        kms = int(command[2])
        cars[car][0] -= kms
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kms} kilometers")

for car, info in cars.items():
    print(f"{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.")