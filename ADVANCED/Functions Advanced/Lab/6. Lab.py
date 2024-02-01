import functools
from functools import reduce

def operate(operator, *args):
    if operator == '+':
        return functools.reduce(lambda a, b: a + b, args)
    elif operator == '-':
        return functools.reduce(lambda a, b: a - b, args)
    elif operator == '*':
        return functools.reduce(lambda a, b: a * b, args)
    elif operator == '/':
        return functools.reduce(lambda a, b: a / b, args)


print(operate("+", 1, 2, 3))