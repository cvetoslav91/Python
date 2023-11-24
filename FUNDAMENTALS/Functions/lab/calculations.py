# "multiply", "divide", "add", "subtract".
def calculations (first_number, second_number, operation):
    if operation == 'multiply':
        result = first_number * second_number
        return result
    elif operation == 'divide':
        result = first_number // second_number
        return result
    elif operation == 'add':
        result = first_number + second_number
        return result
    elif operation == 'subtract':
        result = first_number - second_number
        return result


operation = input()
first_number = int(input())
second_number = int(input())
print(calculations(first_number, second_number, operation))
