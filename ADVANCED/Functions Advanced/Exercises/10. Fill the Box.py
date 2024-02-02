def fill_the_box(*args):
    size_of_the_box = args[0] * args[1] * args[2]
    for i in range(3, len(args)):
        if args[i] == 'Finish':
            if size_of_the_box > 0:
                return f'There is free space in the box. You could put {size_of_the_box} more cubes.'
            else:
                return f'No more free space! You have {abs(size_of_the_box)} more cubes.'
        size_of_the_box -= args[i]


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))