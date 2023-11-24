first_row = input().split()   # 1 0 1
second_row = input().split()  # 1 0 1
third_row = input().split()
first = False
second = False
if first_row[0] == '1' and first_row[1] == '1' and first_row[2] == '1':
    first = True
elif first_row[0] == '1' and second_row[0] == '1' and third_row[0] == '1':
    first = True
elif second_row[0] == '1' and second_row[1] == '1' and second_row[2] == '1':
    first = True
elif first_row[1] == '1' and second_row[1] == '1' and third_row[1] == '1':
    first = True
elif third_row[0] == '1' and third_row[1] == '1' and third_row[2] == '1':
    first = True
elif first_row[2] == '1' and second_row[2] == '1' and third_row[2] == '1':
    first = True
elif first_row[0] == '1' and second_row[1] == '1' and third_row[2] == '1':
    first = True
elif first_row[2] == '1' and second_row[1] == '1' and third_row[0] == '1':
    first = True
elif first_row[0] == '2' and first_row[1] == '2' and first_row[2] == '2':
    second = True
elif first_row[0] == '2' and second_row[0] == '2' and third_row[0] == '2':
    second = True
elif second_row[0] == '2' and second_row[1] == '2' and second_row[2] == '2':
    second = True
elif first_row[1] == '2' and second_row[1] == '2' and third_row[1] == '2':
    second = True
elif third_row[0] == '2' and third_row[1] == '2' and third_row[2] == '2':
    second = True
elif first_row[2] == '2' and second_row[2] == '2' and third_row[2] == '2':
    second = True
elif first_row[0] == '2' and second_row[1] == '2' and third_row[2] == '2':
    second = True
elif first_row[2] == '2' and second_row[1] == '2' and third_row[0] == '2':
    second = True
if not first and not second:
    print('Draw!')
if first:
    print('First player won')
if second:
    print('Second player won')

