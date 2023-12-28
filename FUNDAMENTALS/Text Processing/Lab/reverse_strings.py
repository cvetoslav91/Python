while True:
    command = input()
    if command == 'end':
        break
    result = command[::-1]
    print(f'{command} = {result}')