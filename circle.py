class CircleIterator():
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.index = 0

    def __next__(self):
        if self.index >= self.number:
            raise StopIteration
        iterated_data = getattr(self, self.returns)
        print(iterated_data)
        output = iterated_data[self.index % len(iterated_data)]
        #output = self.seq[self.index % len(self.seq)]
        self.index += 1
        return output

    def __iter__(self):
        print(type(self))
        return type(self)(self.seq, self.number)

class Circle(CircleIterator):
    def __init__(self, seq, number):
        super().__init__(seq, number)
        self.returns = 'seq'

c = Circle('abc', 5)
print(list(c))
print(list(c))

