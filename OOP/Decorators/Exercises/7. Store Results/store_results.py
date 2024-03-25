def store_results(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        x = f"Function '{func.__name__}' was called. Result: {result}\n"
        with open('results.txt', 'a') as file:
            file.write(x)
        return x

    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)