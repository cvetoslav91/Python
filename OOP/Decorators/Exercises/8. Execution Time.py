import time


def exec_time(func):

    def wrapper(*args, **kwargs):
        begin = time.time()
        time.sleep(5)
        result = func(*args, **kwargs)
        end = time.time()
        execute_time = end - begin
        return execute_time

    return wrapper

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))