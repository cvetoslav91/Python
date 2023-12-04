string = input()
list_of_string = [x for x in string]
numbers_list = [int(x) for x in list_of_string if x.isdigit()]
non_numbers_list = [x for x in list_of_string if not x.isdigit()]
take_list = [numbers_list[x] for x in range(len(numbers_list)) if x % 2 == 0]
skip_list = [numbers_list[x] for x in range(len(numbers_list)) if x % 2 == 1]
final_list = []
for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]
    char_taken = non_numbers_list[0:take]
    final_list.append("".join(char_taken))
    skip_char = non_numbers_list[take:take + skip]
    non_numbers_list = non_numbers_list[take + skip:]
result = [x for x in final_list if x]
print(''.join(result))


