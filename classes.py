class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoops = 3
    def __init__(self, *scoops):
        self.scoops = []
        for scoop in scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scoop)

class Bigbowl(Bowl):
    max_scoops = 5

class Envelope():
    postage_multiplier = 10
    def __init__(self, weight):
        self.weight = 0.0
        self.postage = 0
        self.was_sent = False
    def send(self):
        if self.postage >= postage_needed(self):
            self.was_sent = True
    def add_postage(self, postage):
        self.postage += postage
    def postage_needed(self):
        return self.weight * self.postage_multiplier

class BigEnvelope(Envelope):
    postage_multiplier = 15

class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def dial(self, number):
        return f"DIALING {number}"
class SmartPhone(Phone):
    def run_app(self):
        print("running app")
class iphone(SmartPhone):
    def dial(self, number):
        return super().dial(number).lower()

iphonex = iphone("Apple", "Pro")
print(iphonex.dial("911"))
def create_scoop():
    scoops = [Scoop(f) for f in ("choc", "vanilla", "straw") ]
    for scoop in scoops:
        print(scoop.flavor)

class Bread():
    #nutrition = {"carbs": 10, "sugar": 20, "calories": 40}
    def __init__(self):
        self.calories = 100
        self.carbs = 30
        self.sugars = 40
        self.fat = 2

    def get_nutrition(self, slices):
        return {k: v * slices for k, v in vars(self).items()}

class RyeBread(Bread):
    nutrition = {"carbs": 12, "sugar": 10, "calories": 30}

class WholeWheat(Bread):
    {"carbs": 20, "sugar": 10, "calories": 55}

class FlexibleDict(dict):
    def __getitem__(self, item):
        try:
            if item in self:
                key = item
            elif str(item) in self:
                key = str(item)
            elif int(item) in self:
                key = int(item)
        except ValueError:
            pass
        return dict.__getitem__(self, key)

fd = FlexibleDict()
fd['a'] = 100
print(fd['a'])
fd[5] = 500
print(fd[5])
fd[1] = 100
print(fd['1'])
fd['1'] = 100
print(fd[1])

class StringKeyDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

class RecentDict(dict):
    def __init__(self, size):
        super().__init__()
        self.size = size
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

        if len(self) > self.size:
            self.pop(list(self.keys())[0])

class FlatList(list):
    def append(self, obj):
        if iter(obj):
            for element in obj:
                list.append(self, element)
        else:
            list.append(self, obj)
class Animal():
    def __init__(self, color):
        self.color = color
        self.no_of_legs = self.no_of_legs
        self.species = self.__class__.__name__

    def __repr__(self):
        return f"{self.species} {self.color} {self.no_of_legs} legs"

class TwoLegged(Animal):
    no_of_legs = 2
    #def __init__(self, color):

     #   super().__init__(color, TwoLegged.no_of_legs)
class FourLegged(Animal):
    no_of_legs = 4

class ZeroLegged(Animal):
    no_of_legs = 0


class Wolf(FourLegged):
    sound = "Howl"
    size = 10

class Sheep(FourLegged):
    sound = "Baa"
    size = 9

class Snake(ZeroLegged):
    sound = "hiss"
    size = 5

class Parrot(TwoLegged):
    sound = "BC"
    size = 2
class NotCompatibleAnimalsError(Exception):
    pass
class Cage():
    compatible_animals = {Wolf: [Wolf, Snake], Sheep: [Sheep, Parrot, Snake], Parrot: [Sheep, Parrot],
                          Snake: [Snake, Wolf, Sheep]}

    max_animals = 3
    def __init__(self, uid, capacity):
        self.uid = uid
        self.animals = []
        self.capacity = capacity
    def compatibility_check(self, animal):
        for caged_animal in self.animals:
            if type(animal) not in Cage.compatible_animals[type(caged_animal)]:
                raise NotCompatibleAnimalsError(f'{type(animal)} is not compatible with {type(caged_animal)}')
        return True
    def add_animals(self, *animals):
        for animal in animals:
            if len(self.animals) == 0:
                self.animals.append(animal)
            else:
                if  self.compatibility_check(animal):
                    self.animals.append(animal)


            #if self.remaining_capacity() >= animal.size:
             #   self.animals.append(animal)
            #else:
             #   raise NotEnoughSpaceError(f'Not enough room for {animal}')
    def remaining_capacity(self):
        return self.capacity - sum(animal.size for animal in self.animals)
    def __repr__(self):
        output = f"Cage {self.uid} contains \n"
        output += '\n'.join('\t' + str(animal) for animal in self.animals)
        return output
compatible_animals = {Wolf: [Wolf, Snake, Parrot], Sheep: [Sheep, Parrot, Snake], Parrot: [Wolf, Sheep, Parrot], Snake: [Snake, Wolf, Sheep]}
class NotEnoughSpaceError(Exception):
    pass
class BigCage(Cage):
    max_animals = 5

class Zoo():
    def __init__(self, name):
        self.name = name
        self.cages = []
    def add_cage(self, *cages):
        for cage in cages:
            self.cages.append(cage)
    def __repr__(self):
        output = "The zoo contains the following animals: \n"
        for cage in self.cages:
            output += str(cage)
        return output
    def animals_by_legs(self, no_of_legs):
        return [animal for cage in self.cages for animal in cage.animals if animal.no_of_legs == no_of_legs]

    def number_of_legs(self):
        return sum(animal.no_of_legs for cage in self.cages for animal in cage.animals)

w = Wolf("Grey")
p = Parrot("Red")
print(w)
print(p)
c1 = Cage(1, 200)
c1.add_animals(w, w, w)
print(c1)

z = Zoo("Houston")
z.add_cage(c1)
print(z.animals_by_legs(4))
print(z)
print(z.number_of_legs())
create_scoop()