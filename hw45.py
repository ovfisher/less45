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

staff = []
#animals = []

class Zookeeper:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def feed(self,animal):
        print('fed')
# staff - user's list

class Zoovet:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def heal(self,animal):
        print('healed')

class Zoo:
    def __init__(self,addr):
        self.addr = addr

    def add_animal(self,animal):
        animals.append(animal)
        #add_animal = f'{self.get_user_info()}'
        print(f'added - {animal.name}')

    def remove_animal(self, animal):
        animals.remove(animal)            # remove_staff = f'{self.get_user_info()}'
        print(f'removed - {animal.name}')

    def add_staff(self,person):
        staff.append(person)
        #add_animal = f'{self.get_user_info()}'
        print(f'added - {person.name}')

    def remove_staff(self,person):
        staff.remove(person)
        #remove_staff = f'{self.get_user_info()}'
        print(f'removed - {person.name}')

zoo = Zoo('Blunenstrsse')
zkeeper = Zookeeper(len(staff),'Basil')
zoo.add_staff(zkeeper)
zvet = Zoovet(len(staff),'Masha')
zoo.add_staff(zvet)
animals = []
bird = Bird('b1',2)
zoo.add_animal(bird)
snake = Reptile('python',100)
zoo.add_animal(snake)
zvet.heal(snake)
zkeeper.feed(bird)
