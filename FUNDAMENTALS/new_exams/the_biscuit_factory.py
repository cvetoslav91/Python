from math import floor
biscuits_per_day = int(input())
workers = int(input())
buscuits_of_competing_factory = int(input())
total_biscuits = 0
for day in range(1, 30):
    daily_biscuits = biscuits_per_day * workers
    third_day_biscuits = floor(daily_biscuits * 0.75)
    total_biscuits = (daily_biscuits * 20) + (third_day_biscuits * 10)
print(f'You have produced {total_biscuits} biscuits for the past month.')
difference = abs(total_biscuits - buscuits_of_competing_factory)
if total_biscuits > buscuits_of_competing_factory:
    percent = (difference / buscuits_of_competing_factory) * 100
    print(f'You produce {percent:.2f} percent more biscuits.')
else:
    percent = (difference / buscuits_of_competing_factory) * 100
    print(f'You produce {percent:.2f} percent less biscuits.')