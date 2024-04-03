def valid_index(index, text):
    if 0 <= index < len(text):
        return True
    return False


def letters(text, command):
    if command == 'Upper':
        return text.upper()
    elif command == 'Lower':
        return text.lower()


def reverse(text, start_index, end_index):
    if valid_index(start_index, text) and valid_index(end_index, text):
        result = text[start_index:end_index + 1]
        result = result[::-1]
        return result
    return False


def substring(text, sub):
    if sub in text:
        text = text.replace(sub, '')
        return text
    return False


def replace(text, char):
    text = text.replace(char, '-')
    return text


def is_valid(text, char):
    if char in text:
        return True
    return False

username = input()

while True:
    command = input().split()

    if command[0] == 'Registration':
        break

    elif command[0] == 'Letters':
        username = letters(username, command[1])
        print(username)

    elif command[0] == 'Reverse':
        result = reverse(username, int(command[1]), int(command[2]))
        if result:
            print(result)
        else:
            continue

    elif command[0] == 'Substring':
        result = substring(username, command[1])
        if result:
            username = result
            print(username)
        else:
            print(f"The username {username} doesn't contain {command[1]}.")

    elif command[0] == 'Replace':
        username = replace(username, command[1])
        print(username)

    elif command[0] == 'IsValid':
        result = is_valid(username, command[1])
        if result:
            print(f"Valid username.")
        else:
            print(f"{command[1]} must be contained in your username.")
