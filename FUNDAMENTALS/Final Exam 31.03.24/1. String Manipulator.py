def translate(text, char, replacement):
    return text.replace(char, replacement)


def includes(text, substring):
    if substring in text:
        return True
    return False


def start(text, substring):
    if text.startswith(substring):
        return True
    return False


def find_index(text, char):
    for c in range(len(text) - 1, -1, -1):
        if text[c] == char:
            return c


def remove(text, start_index, count):
    text = text[:start_index] + text[start_index + count:]
    return text



string = input()

while True:

    command = input().split()

    if command[0] == 'End':
        break

    elif command[0] == 'Translate':
        string = translate(string, command[1], command[2])
        print(string)

    elif command[0] == 'Includes':
        if includes(string, command[1]):
            print('True')
        else:
            print('False')

    elif command[0] == 'Start':
        if start(string, command[1]):
            print('True')
        else:
            print('False')

    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)

    elif command[0] == 'FindIndex':
        print(find_index(string, command[1]))

    elif command[0] == 'Remove':
        string = remove(string, int(command[1]), int(command[2]))
        print(string)