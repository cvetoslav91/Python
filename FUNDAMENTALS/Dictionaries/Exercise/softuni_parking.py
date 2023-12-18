n = int(input())
dictionary = {}
for current_reg in range(n):
    command = input().split()
    if command[0] == 'register':
        name = command[1]
        plate_number = command[2]
        if name not in dictionary:
            dictionary[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif command[0] == 'unregister':
        name = command[1]
        if name not in dictionary:
            print(f"ERROR: user {name} not found")
        else:
            del dictionary[name]
            print(f"{name} unregistered successfully")
for key, value in dictionary.items():
    print(f'{key} => {value}')