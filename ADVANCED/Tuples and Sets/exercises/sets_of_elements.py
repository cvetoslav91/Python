n, m = input().split()
n_set = set()
m_set = set()
for _ in range(int(n)):
    number = input()
    n_set.add(number)

for _ in range(int(m)):
    number = input()
    m_set.add(number)

result = n_set.intersection(m_set)
print(*result, sep='\n')