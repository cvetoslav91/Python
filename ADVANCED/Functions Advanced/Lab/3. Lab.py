def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for i in sorted_dict:
        result += f'{i[0]}\n'
        for j in sorted(i[1], reverse=True):
            result += f'{j}\n'
    return result



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)