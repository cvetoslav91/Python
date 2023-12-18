dictionary = {}
while True:
    name = input()
    if '-' not in name:
        break
    name, number = name.split('-')
    dictionary[name] = number

name = int(name)
for i in range(name):
    search_name = input()
    if search_name in dictionary.keys():
        print(f"{search_name} -> {dictionary[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")