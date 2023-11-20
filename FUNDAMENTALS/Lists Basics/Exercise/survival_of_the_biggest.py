integers = input()
number_of_deleted_items = int(input())
my_list = integers.split(' ')
new_list = list(map(int, my_list))
for i in range(number_of_deleted_items):
    minimum_number = min(new_list)
    new_list.remove(minimum_number)
for j in new_list:
    if j == new_list[-1]:
        print(j)
    else:
        print(j, end=', ')