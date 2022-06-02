class Iterator:
    def __init__(self):
        self.index = 0
        self.value = list(range(10))
        print(self.value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.value):
            raise StopIteration
        value = self.value[self.index]
        self.index += 1
        return value


iter_obj = Iterator()
for i in iter_obj:
    print(i)
