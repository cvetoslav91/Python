def math_operations(*args, **kwargs):
    list_of_keys = list(kwargs.keys())
    for i in range(len(args)):
        key = list_of_keys[i % 4]
        if key == 'a':
            kwargs['a'] += args[i]
        elif key == 's':
            kwargs['s'] -= args[i]
        elif key == 'd' and args[i] != 0:
            kwargs['d'] /= args[i]
        elif key == 'm':
            kwargs['m'] *= args[i]
    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return ''.join(f'{i[0]}: {i[1]:.1f}\n' for i in result)

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))