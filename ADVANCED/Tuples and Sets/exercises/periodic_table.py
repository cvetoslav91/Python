n = int(input())
elements = set()

for _ in range(n):
    new_el = input().split()
    for el in new_el:
        elements.add(el)

print(*elements, sep='\n')