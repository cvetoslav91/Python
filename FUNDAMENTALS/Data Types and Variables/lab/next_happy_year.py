year = int(input())
while True:
    year += 1
    year = str(year)
    set_year = set(year)
    if len(year) == len(set_year):
        print(year)
        break
    year = int(year)
