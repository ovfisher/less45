class   Animal():
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав")

class Cat(Animal):
    def make_sound(self):
        print("мяу")

class Cow(Animal):
    def make_sound(self):
        print("мууу")

dog = Dog()
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()