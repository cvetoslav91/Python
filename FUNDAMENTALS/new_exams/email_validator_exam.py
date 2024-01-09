mail = input()

while True:
    command = input()
    if command == 'Complete':
        break
    if command == "Make Upper":
        mail = mail.upper()
        print(mail)
    elif command == "Make Lower":
        mail = mail.lower()
        print(mail)
    elif "GetDomain" in command:
        name, count = command.split()
        count = int(count)
        rev = mail[-1:-(count+1):-1]
        print(rev[-1::-1])
    elif command == "GetUsername":
        if '@' in mail:
            index = mail.index('@')
            print(mail[:index])
        else:
            print(f"The email {mail} doesn't contain the @ symbol.")
    elif 'Replace' in command:
        name, char = command.split()
        mail = mail.replace(char, '-')
        print(mail)
    elif command == 'Encrypt':
        result = [ord(char) for char in mail]
        print(' '.join(map(str, result)))

