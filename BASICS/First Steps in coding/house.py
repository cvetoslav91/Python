x = float(input())
y = float(input())
h = float(input())

door = (x * x - 2.4)
window = ((x * y) - 2.25) * 2
wall = x * x

total = window + door + wall
green_paint = total / 3.4

form_green = f'{green_paint:.2f}'

front = x * h
roof = x * y * 2
total_size = roof + front

red = total_size / 4.3

form_red = f'{red:.2f}'

print(form_green)
print(form_red)