first_string = input().split(', ')
second_string = input().split()
list = []
for word in first_string:
    for match in second_string:
        if word in match:
            if word not in list:
                list.append(word)
print(list)