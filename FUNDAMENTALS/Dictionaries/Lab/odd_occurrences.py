elements = input().split()
dictionary = {}
for current_element in elements:
    current_element = current_element.lower()
    if current_element in dictionary:
        dictionary[current_element] += 1
    else:
        dictionary[current_element] = 1
for key, value in dictionary.items():
    if value % 2 == 1:
        print(key, end=' ')