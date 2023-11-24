def characters(password):
    password = list(password)
    for char in password:
        if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            valid = True
        else:
            valid = False
            break
    if valid:
        return True

def digits(password):
    password = list(password)
    counter = 0
    for char in password:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' \
            or char == '6' or char == '7' or char == '8' or char == '9':
            counter += 1
            if counter == 2:
                return True



def password_validator(password):
    ok = True
    list_of_messages = []
    if 6 > len(password) or len(password) > 10:
        ok = False
        print("Password must be between 6 and 10 characters")
    if characters(password) is not True:
        ok = False
        print("Password must consist only of letters and digits")
    if digits(password) is not True:
        ok = False
        print("Password must have at least 2 digits")
    if ok:
        print('Password is valid')
    return ''
password = input()
print(password_validator(password))

