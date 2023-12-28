string = input().split()
for word in string:
    result = word * len(word)
    print(result, end="")