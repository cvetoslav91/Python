import re
from collections import deque

numbers = deque()
total_results = []

string = input().split()

for char in string:
    if re.findall(r'\-?\d', char):
        numbers.append(int(char))
    elif char == '+':
        if total_results:
            first_number = total_results.pop()
        else:
            first_number = numbers.popleft()
        while numbers:
            first_number += numbers.popleft()
        total_results.append(first_number)
    elif char == '-':
        if total_results:
            first_number = total_results.pop()
        else:
            first_number = numbers.popleft()
        while numbers:
            first_number -= numbers.popleft()
        total_results.append(first_number)
    elif char == '*':
        if total_results:
            first_number = total_results.pop()
        else:
            first_number = numbers.popleft()
        while numbers:
            first_number *= numbers.popleft()
        total_results.append(first_number)
    elif char == '/':
        if total_results:
            first_number = total_results.pop()
        else:
            first_number = numbers.popleft()
        while numbers:
            first_number /= numbers.popleft()
        total_results.append(int(first_number))

print(*total_results)