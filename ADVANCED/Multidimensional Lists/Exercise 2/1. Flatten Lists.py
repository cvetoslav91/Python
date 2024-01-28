import re

numbers = re.split(' *\| *', input())
for i in range(len(numbers) - 1, -1, -1):
    result = numbers[i].split()
    for num in result:
        print(num, end=' ')
