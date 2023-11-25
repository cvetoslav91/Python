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


type = input()
value = input()
print(data_type(type, value))