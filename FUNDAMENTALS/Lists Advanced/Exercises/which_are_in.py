first_string = input().split(', ')
second_string = input().split()
# for word in first_string:
#     for match in second_string:
#         if word in match:
#             if word not in list:
#                 list.append(word)
# print(list)
final_list = []
my_list = [word for word in first_string for match in second_string if word in match]
for i in my_list:
    if i not in final_list:
        final_list.append(i)
print(final_list)