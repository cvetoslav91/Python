class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.index = -1
        self.only_vowels = [v for v in self.string if v.lower() in self.vowels]


    def __iter__(self):
        return self


    def __next__(self):
        self.index += 1
        if self.index < len(self.only_vowels):
            return self.only_vowels[self.index]
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)