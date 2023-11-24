numbers = input().split()
string = input()
string = list(string)
current_sum = 0
final_list = []
for whole_number in numbers:
    for number in whole_number:
        current_sum += int(number)
    while current_sum >= len(string):
        current_sum -= len(string)
    letter = string.pop(current_sum)
    current_sum = 0
    final_list.append(letter)
for i in final_list:
    print(f'{i}', end='')
