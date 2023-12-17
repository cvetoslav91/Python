countries = input().split(', ')
capitals = input().split(', ')
dictionary = zip(countries, capitals)
dictionary = dict(dictionary)
for key, value in dictionary.items():
    print(f'{key} -> {value}')