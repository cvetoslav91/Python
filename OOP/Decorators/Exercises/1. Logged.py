def logged(function):

    def wrapper(*args):

        result = f'you called {function.__name__}{tuple(args)}\n'
        f = function(*args)
        result += f'it returned {f}'
        return result

    return wrapper



@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))