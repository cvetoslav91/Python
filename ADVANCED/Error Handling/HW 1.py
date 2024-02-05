numbers_dictionary = {}

line = input()
while line != 'Search':
    try:
        number_as_int = int(input())
        numbers_dictionary[line] = number_as_int
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()
while line != "Remove":
    try:
        searched = numbers_dictionary[line]
        print(searched)
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()
while line != "End":
    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)