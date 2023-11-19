factor = int(input())
count = int(input())
my_list = []
multiplier = factor
for i in range(count):
    my_list.append(factor)
    factor += multiplier
print(my_list)