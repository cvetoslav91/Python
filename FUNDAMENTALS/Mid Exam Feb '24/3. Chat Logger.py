message = []

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'Chat':
        message.append(command[1])

    elif command[0] == 'Delete':
        if command[1] in message:
            message.remove(command[1])

    elif command[0] == 'Edit':
        if command[1] in message:
            index = message.index(command[1])
            message[index] = command[2]

    elif command[0] == 'Pin':
        if command[1] in message:
            moved_message = message.pop(message.index(command[1]))
            message.append(moved_message)

    elif command[0] == 'Spam':
        messages = command[1:]
        message.extend(messages)

print(*message, sep='\n')