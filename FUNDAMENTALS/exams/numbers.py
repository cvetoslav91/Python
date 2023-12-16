numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
above_average = [x for x in numbers if x > average]
if not above_average:
    print('No')
    exit()
above_average.sort(reverse=True)
if len(above_average) > 5:
    above_average = above_average[:5]
print(*above_average)
