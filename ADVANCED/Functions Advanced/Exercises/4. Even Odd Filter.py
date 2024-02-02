def even_odd_filter(**evenodd):
    for key, value in evenodd.items():
        if key == 'even':
            evenodd['even'] = [x for x in value if x % 2 == 0]
        else:
            evenodd['odd'] = [x for x in value if x % 2 != 0]
    return dict(sorted(evenodd.items(), key=lambda x: len(x[1]), reverse=True))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
