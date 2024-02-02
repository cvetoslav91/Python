def concatenate(*args, **kwargs):
    args = ''.join(args)
    for key, value in kwargs.items():
        args = args.replace(key, value)
    return args




print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))