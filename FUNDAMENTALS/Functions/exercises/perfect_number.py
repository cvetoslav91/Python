def perfect_number(number):
    dividers = []
    for curr_number in range(number - 1, 0, -1):
        if number % curr_number == 0:
            dividers.append(curr_number)
    if sum(dividers) == number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."

number = int(input())
print(perfect_number(number))