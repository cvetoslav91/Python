def grocery_store(**products):
    to_print = ''
    result = dict(sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for key, value in result.items():
        to_print += (f'{key}: {value}\n')
    return to_print

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))