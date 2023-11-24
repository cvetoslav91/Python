def only_even(even):
    if even % 2 == 0:
        return True
    return False


numbers = input().split()
list_numbers = list(map(int, numbers))
result = filter(only_even, list_numbers)
result_list = list(result)
print(result_list)

