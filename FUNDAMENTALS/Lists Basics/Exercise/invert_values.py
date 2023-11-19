single_string = input()
my_list = single_string.split()
new_list = list(map(int, my_list))
final_list = []
for number in new_list:
    final_list.append(-number)
print(final_list)