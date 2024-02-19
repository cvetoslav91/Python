def print_rhombus():
    print(' ' * (n - row), end='')
    print(*['*'] * row)

n = int(input())

for row in range(1, n + 1):
    print_rhombus()

for row in range(n - 1, 0, -1):
    print_rhombus()