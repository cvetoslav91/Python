def loading_bar(number):
    symbols = number // 10
    percents = f'{number}%'
    points = 10 - symbols
    if number == 100:
        print('100% Complete!')
        return '[%%%%%%%%%%]'
    else:
        print(percents, end=' ')
        print('[', end="")
        print('%' * symbols, end="")
        print('.' * points, end='')
        print(']')

        return "Still loading..."

number = int(input())
print(loading_bar(number))