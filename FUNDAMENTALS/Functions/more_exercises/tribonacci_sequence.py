def tribonacci(n):
    current_list = [1, 1, 2]
    full_list = [1, 1, 2]
    for i in range(n - 3):
        sum_of_last_three = sum(current_list)
        new_number = sum_of_last_three
        current_list.insert(3, new_number)
        current_list.pop(0)
        full_list.append(new_number)
    return full_list

number = int(input())
if number == 1:
    print(number)
elif number == 2:
    print('1 1')
else:
    print(*tribonacci(number))
