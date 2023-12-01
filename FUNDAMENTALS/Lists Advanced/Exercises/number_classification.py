numbers = list(map(int, input().split(', ')))
positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]
even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]
print(f'Positive: ', end="")
print(*positive, sep=', ')
print(f'Negative: ', end='')
print(*negative, sep=', ')
print(f'Even: ', end="")
print(*even, sep=', ')
print(f'Odd: ', end="")
print(*odd, sep=', ')