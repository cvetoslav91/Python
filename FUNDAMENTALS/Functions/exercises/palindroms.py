def palindrome(number):
    reversed_number = number[::-1]
    if number == reversed_number:
        return True
    return False

numbers = input().split(', ')
for number in numbers:
    if palindrome(number):
        print('True')
    else:
        print('False')