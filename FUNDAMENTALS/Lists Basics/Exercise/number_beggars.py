values = input()
list_of_values = values.split(', ')
new_list = list(map(int, list_of_values))
beggars = int(input())
output_list = []
for current_beggar in range(beggars):
    current_sum = 0
    for i in range(current_beggar, len(new_list), beggars):
        number = new_list[i]
        current_sum += number
    output_list.append(current_sum)
print(output_list)

