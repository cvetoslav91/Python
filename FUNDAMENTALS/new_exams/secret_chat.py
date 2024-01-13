message = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    instructions = command.split(':|:')
    if instructions[0] == 'InsertSpace':
        index = int(instructions[1])
        message = message[:index] + ' ' + message[index:]
    elif instructions[0] == 'Reverse':
        substring = instructions[1]
        if substring in message:
            message = message.replace(substring, '')
            message = message + substring[-1::-1]
        else:
            print('error')
            continue
    elif instructions[0] == 'ChangeAll':
        substring = instructions[1]
        replacement = instructions[2]
        message = message.replace(substring, replacement)
    print(message)
print(f"You have a new text message: {message}")