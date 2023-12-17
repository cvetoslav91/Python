n = int(input())
dictionary = {}
for i in range(n):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)


for key, value in dictionary.items():
    string = ', '.join(value)
    print(f'{key} - {string}')