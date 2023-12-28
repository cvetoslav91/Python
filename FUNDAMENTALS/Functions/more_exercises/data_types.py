def data_type(type, value):
    if type == 'int':
        value = int(value)
        return value * 2
    elif type == 'real':
        value = float(value)
        result = value * 1.5
        return f'{result:.2f}'
    elif type == 'string':
        return f'${value}$'


type_of_data = input()
number = input()
print(data_type(type_of_data, number))
