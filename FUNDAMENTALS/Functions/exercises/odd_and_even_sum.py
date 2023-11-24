def odd_and_even_sum(number):
    sum_even = 0
    sum_odd = 0
    number = list(number)
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    return sum_even, sum_odd

number = input()
result = odd_and_even_sum(number)
result = list(result)
print(f'Odd sum = {result[1]}, Even sum = {result[0]}')