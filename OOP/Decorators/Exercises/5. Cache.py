def cache(func):
    log = {}

    def wrapper(number):
        if number not in log:
            log[number] = func(number)
        return log[number]

    wrapper.log = log

    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



fibonacci(3)
fibonacci(5)
print(fibonacci.log)
