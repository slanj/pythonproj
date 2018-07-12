class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print(self.name, "says: ", "You are idiots!")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
    def speak(self):
        print(self.name, "says: ", "You are doomed!")
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)

class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('Shut up and take my money')
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

hedgehog = Animal(42)
hedgehog.set_name("Bill")
print(hedgehog)

barsik = Cat(42)
barsik.set_name('Barsik')
barsik.speak()
print(barsik)

bart = Human("Bart", 55)
hanry = Human("Hanry", 42)
hanry.age_diff(bart)
hanry.speak()
print(hanry)