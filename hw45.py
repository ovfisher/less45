class   Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        print("___")

class Bird(Animal):
    def make_sound(self):
        print("twit")
    def eat(self):
        print("wheat")

class Mammal(Animal):
    def make_sound(self):
        print("Pooo")
    def eat(self):
        print("milk")

class Reptile(Animal):
    def make_sound(self):
        print("Fooo")
    def eat(self):
        print("grass")

bird = Bird('b1',2)
animals = [bird, Mammal('m1',3), Reptile('R1',4)]
for animal in animals:
    animal.make_sound()