def take_odd(text):
    new_text = [text[ch] for ch in range(len(text)) if ch % 2 == 1]
    return ''.join(new_text)


def cut(text, index, length):
    return text[:index] + text[index + length:]


def substitute_text(text, substring, substitute):
    if substring in text:
        return text.replace(substring, substitute)


text = input()

while True:
    command = input().split()

    if command[0] == 'Done':
        print(f"Your password is: {text}")
        break

    elif command[0] == 'TakeOdd':
        text = take_odd(text)

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        text = cut(text, index, length)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = substitute_text(text, substring, substitute)
        else:
            print('Nothing to replace!')
            continue

    print(text)
