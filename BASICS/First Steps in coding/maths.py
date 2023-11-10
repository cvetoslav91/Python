from math import pi

type = input()

if type == 'square':
    a = float(input())
    S = a * a
    print(f'{S:.3f}')

elif type == 'rectangle':
    a = float(input())
    b = float(input())
    S = a * b
    print(f'{S:.3f}')


elif type == 'circle':
    r = float(input())
    S = pi * r * r
    print(f'{S:.3f}')

elif type == 'triangle':
    a = float(input())
    h = float(input())
    S = a * h / 2
    print(f'{S:.3f}')
