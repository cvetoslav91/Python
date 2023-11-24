single_string = input().split(', ')
counter = 0
copy_string = single_string.copy()
for number in copy_string:
    if number == '0':
        single_string.remove('0')
        counter += 1
for _ in range(counter):
    single_string.append('0')
single_string = list(map(int, single_string))
print(single_string)
