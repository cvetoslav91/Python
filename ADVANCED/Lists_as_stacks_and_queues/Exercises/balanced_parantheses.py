from collections import deque

source = input()

open_par = []
close_par = []
for char in source:
    if char == '(' or char == '[' or char == '{':
        open_par.append(char)
    else:
        if len(open_par) == 0:
            print('NO')
            exit()
        last_par = open_par.pop()
        if (char == ')' and last_par == '(') or (char == ']' and last_par == '[') or (char == '}' and last_par == '{'):
            continue
        else:
            print('NO')
            exit()

print('YES')