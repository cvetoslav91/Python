class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start <= self.count:
            return self.step * (self.start - 1)
        else:
            raise StopIteration

numbers = take_skip(10, 5)
for number in numbers:
    print(number)