n = int(input())
results = []
for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = first.split(',')
    first_start = int(first_start)
    first_end = int(first_end)
    second_start, second_end = second.split(',')
    second_start = int(second_start)
    second_end = int(second_end)
    first_set = set(int(x) for x in range(first_start, first_end + 1))
    second_set = set(int(x) for x in range(second_start, second_end + 1))
    result = first_set.intersection(second_set)
    results.append(result)

max_intersections = [len(x) for x in results]
max_number = max(max_intersections)
index = max_intersections.index(max_number)
print(f'Longest intersection is {list(results[index])} with length {max_number}')
