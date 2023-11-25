a = int(input())
b = int(input())
c = int(input())
my_list = []
my_list.append(a)
my_list.append(b)
my_list.append(c)
counter = 0
zero = False
for i in my_list:
    if i == 0:
        zero = True
        break
    if i > 0:
        pass
    if i < 0:
        counter += 1
if zero:
    print('zero')
elif counter % 2 == 1:
    print('negative')
else:
    print('positive')