from collections import deque

string = deque(input().split())
time_of_found = []
colors_found = []
sec_colors = []
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
while string:
    substring_1 = string.popleft()
    if string:
        substring_2 = string.pop()
    else:
        substring_2 = ""
    x = substring_1 + substring_2
    y = substring_2 + substring_1
    if x in main_colors:
        colors_found.append(x)
        time_of_found.append(x)
    elif x in secondary_colors:
        sec_colors.append(x)
        time_of_found.append(x)
    elif y in main_colors:
        colors_found.append(y)
        time_of_found.append(y)
    elif y in secondary_colors:
        sec_colors.append(y)
        time_of_found.append(y)
    else:
        new_string_1 = substring_1[:-1]
        new_string_2 = substring_2[:-1]
        index = len(string) // 2
        if new_string_1:
            string.insert(index, new_string_1)
        if new_string_2:
            string.insert(index, new_string_2)
secondary_colors_found = []
for color in sec_colors:
    if color == 'orange':
        if 'red' in colors_found and 'yellow' in colors_found:
            secondary_colors_found.append(color)
    elif color == 'purple':
        if 'red' in colors_found and 'blue' in colors_found:
            secondary_colors_found.append(color)
    elif color == 'green':
        if 'blue' in colors_found and 'yellow' in colors_found:
            secondary_colors_found.append(color)
final_list = []
total_founds = colors_found + secondary_colors_found
for color in time_of_found:
    if color in total_founds:
        final_list.append(color)

print(final_list)