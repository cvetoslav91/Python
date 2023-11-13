strings = int(input())
open_bracket = False
close_bracket = False
balanced = bool
last_bracket = ''
break_condition = False
for i in range(strings):
    new_string = input()
    if new_string == '(':
        if last_bracket == '(':
            balanced = False
            break_condition = True
        last_bracket = '('
        balanced = False
    elif new_string == ')':
        if last_bracket == '(':
            balanced = True
        elif last_bracket == ')' or last_bracket == '':
            balanced = False
            break_condition = True
        last_bracket = ')'
if balanced and not break_condition:
    print('BALANCED')
else:
    print('UNBALANCED')