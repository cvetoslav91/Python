n = input()
my_list = n.split(' ')
splits = int(input())
new_list = []
index = len(my_list) // 2
first_half = my_list[:index]
second_half = my_list[index:]
current_list = []
for i in range(splits):
    while len(first_half) != 0:
        number = first_half.pop(0)
        current_list.append(number)
        number = second_half.pop(0)
        current_list.append(number)
    first_half = current_list[:index]
    second_half = current_list[index:]
    new_list = current_list
    current_list = []
print(new_list)