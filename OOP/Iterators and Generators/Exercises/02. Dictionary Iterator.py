class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = [key for key in dictionary.keys()]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.keys):
            current_key = self.keys[self.index]
            return current_key, self.dictionary[current_key]
        else:
            raise StopIteration



result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)