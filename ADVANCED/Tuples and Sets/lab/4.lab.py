n = int(input())
parking = set()
for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        parking.add(number)
    elif command == 'OUT':
        parking.remove(number)

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")