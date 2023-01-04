class MyEnumerate():
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable
        print(id(self))

    def __iter__(self):
        return self
    def __next__(self):

        if self.index >= len(self.iterable):
            raise StopIteration
        value = (self.index, self.iterable[self.index])
        self.index += 1
        return value

# a helper class version of myenum

class MyEnum():
    def __init__(self, data, index=0):
        self.data = data
        self.index = index
    def __iter__(self):

        x =  MyEnumIterator(self.data, self.index)
        print(f"returning iterator {x}")
        return x

class MyEnumIterator():
    def __init__(self, data, index):
        self.data = data
        self.index = 0
        self.offset = index
        print(id(self))
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        output = (self.index + self.offset, self.data[self.index])
        self.index += 1
        return output
B = MyEnum('xyz', 1)
test = iter(B)
print(f'id of test is {id(test)}')
next(test)
next(test)
next(test)
try:
    next(test)
except StopIteration:
    pass
test = iter(B)
print(f'2nd id of test is {id(test)}')
next(test)
next(test)
next(test)

for i, v in B:
    print(f"{i} {v}")

for i, v in B:
    print(f"{i} {v}")

# myenum as generator function

def myenumgenerator(iterable):
    index = 0
    for x in iterable:
        yield (index, x)
        index += 1

C = myenumgenerator('def')
for element in C:
    print(element)

class Circle():
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
    def __iter__(self):
        return CircleIterator(self.seq, self.number)

class CircleIterator():
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.index = 0
    def __next__(self):
        if self.index >= self.number:
            raise StopIteration
        output = self.seq[self.index % len(self.seq)]
        self.index += 1
        return output
c = Circle('abc', 5)
print(list(c))