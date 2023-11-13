number = int(input())
is_special = True
for i in range(2, number):
    if number % i == 0:
        is_special = False
print(is_special)
