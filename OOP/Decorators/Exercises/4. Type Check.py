def type_check(the_type):

    def decorator(function):

        def wrapper(*args):

            if all([type(x) == the_type for x in args]):
                return function(*args)
            return 'Bad Type'
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'), 'Bad Type')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))