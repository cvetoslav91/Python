from collections import deque

names = deque(input().split())
number = int(input()) - 1

while len(names) > 1:
    names.rotate(-number)
    deleted = names.popleft()
    print(f"Removed {deleted}")

print(f"Last is {''.join(names)}")