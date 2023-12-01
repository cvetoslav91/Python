rooms = int(input())
not_enough_chairs = False
total_free_chairs = 0
for room in range(1, rooms + 1):
    in_room = input().split()
    chairs = in_room[0]
    visitors = int(in_room[1])
    if len(chairs) >= visitors:
        free_chairs = len(chairs) - visitors
        total_free_chairs += free_chairs
        continue
    else:
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
        not_enough_chairs = True
if not not_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
