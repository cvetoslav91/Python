units = input().split() #[1, 2, , 4, 5, , 7]  [0, 1, , 3, 4, , 6, 7, , 9, 10, 11, 12]
copy_units = units.copy()
executer = int(input()) #len = 7
final_list = []
index = 0
for i in range(len(units)): #7 0,1
    index += executer - 1
    while index >= len(units):
        index -= len(units)
    number = units.pop(index)
    final_list.append(number)
print('[', end='')
print(','.join(final_list), end='')
print(']')
