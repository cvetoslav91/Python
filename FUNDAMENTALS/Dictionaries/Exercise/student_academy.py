n = int(input())
dictionary = {}
for current_student in range(n):
    name = input()
    grade = float(input())
    if name not in dictionary:
        dictionary[name] = []
    dictionary[name].append(grade)

for key, value in dictionary.items():
    average = sum(value) / len(value)
    dictionary[key] = average

dictionary_copy = dictionary.copy()
for key, value in dictionary_copy.items():
    if value < 4.50:
        del dictionary[key]
        continue
    else:
        print(f'{key} -> {value:.2f}')
