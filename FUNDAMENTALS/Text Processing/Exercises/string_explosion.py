string = input()
missed = 0
for char in range(len(string)):
    if string[char] == '>':
        print('>', end="")
        missed += int(string[char + 1])
    else:
        if missed == 0:
            print(string[char], end="")
        else:
            missed -= 1