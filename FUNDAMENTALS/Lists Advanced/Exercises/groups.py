def between_numbers(number, first, second):
    if first < number <= second:
        return number


numbers = list(map(int, input().split(', ')))
low_10 = 0
high_10 = 10
while len(numbers) != 0:
    result = [number for number in numbers if between_numbers(number, low_10, high_10)]
    for number in result:
        numbers.remove(number)
    print(f"Group of {high_10}'s: {result}")
    low_10 += 10
    high_10 += 10