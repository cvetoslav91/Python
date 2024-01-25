n = int(input())
odds = set()
evens = set()

for i in range(1, n + 1):
    name = input()
    current_sum = 0
    for char in name:
        current_sum += ord(char)
    final_sum = int(current_sum / i)
    if final_sum % 2 == 0:
        evens.add(final_sum)
    else:
        odds.add(final_sum)
if sum(odds) == sum(evens):
    print(*odds.union(evens), sep=', ')
elif sum(odds) > sum(evens):
    print(*odds.difference(evens), sep=', ')
else:
    print(*odds.symmetric_difference(evens), sep=', ')