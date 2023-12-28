def factorial(factorial, divider):
    if factorial == 0:
        final_result = 1 / divider
        return f'{final_result:.2f}'
    result = 1
    divide_result = 1
    for i in range(2, factorial + 1):
        result *= i
    for j in range(2, divider + 1):
        divide_result *= j
    final_result = result / divide_result
    return f'{final_result:.2f}'


factorial_number = int(input())
divider = int(input())
print(factorial(factorial_number, divider))
