def even_odd(*args):
    even = []
    odd = []
    for i in range(len(args) - 1):
        if args[-1] == 'even':
            if int(args[i]) % 2 == 0:
                even.append(args[i])
        elif args[-1] == 'odd':
            if int(args[i]) % 2 != 0:
                odd.append(args[i])

    if args[-1] == 'even':
        return even
    elif args[-1] == 'odd':
        return odd

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

