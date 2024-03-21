def get_primes(items):
    for num in items:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            if num > 1:
                yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))