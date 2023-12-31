def move(text, value):
    moved = text[:value]
    left = text[value:]
    new_text = left + moved
    return new_text


def insert(text, index, value):
    text_as_list = [x for x in text]
    text_as_list.insert(index, value)
    final_text = ''.join(text_as_list)
    return final_text

def change(text, substring, replacement):
    while substring in text:
        text = text.replace(substring, replacement)
    return text



text = input()

while True:
    command = input()
    if command == 'Decode':
        break
    command_as_list = command.split('|')
    if command_as_list[0] == 'Move':
        text = move(text, int(command_as_list[1]))
    elif command_as_list[0] == 'Insert':
        index = int(command_as_list[1])
        value = command_as_list[2]
        text = insert(text, index, value)
    elif command_as_list[0] == 'ChangeAll':
        substring = command_as_list[1]
        replacement = command_as_list[2]
        text = change(text, substring, replacement)

print(f'The decrypted message is: {text}')