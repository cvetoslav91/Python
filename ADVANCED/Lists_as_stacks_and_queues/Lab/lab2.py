expression = input()
open_par = []
for i in range(len(expression)):
    if expression[i] == '(':
        open_par.append(i)
    elif expression[i] == ')':
        print(expression[open_par.pop():i + 1])
