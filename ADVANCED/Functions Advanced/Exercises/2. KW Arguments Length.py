def kwargs_length(**kwargs):
    total = 0
    for i in kwargs:
        total += 1
    return total

dictionary = {}

print(kwargs_length(**dictionary))