class Engine:
    def __init__(self,power):
        self.power = power

class Car:
    def __init__(self,model,engine):
        self.model = model
        self.engine = engine    # aggregation

engine = Engine(200)
car = Car('Gaz',engine)
#Объект класса Engine создается отдельно — не внутри класса Car
#После этого можно использовать объект класса (self.engine) внутри класса Car.
#Агрегация. Если удалить класс машины, то объект класса engine не пропадет.

#Композиция
class Motor:
    def start(self):
        print('Двигатель запущен')

    def stop(self):
        print('Двигатель остановлен')

class Auto:
    def __init__(self):
        self.motor = Motor() #Motor — класс, motor — переменная, в которую сохраняется объект класса.
#был создан объект класса внутри другого класса — настроена строгая взаимосвязь.
    def start(self):
        self.motor.start()

    def stop(self):
        self.motor.stop()
#Строгая связь настроена так, что машина вообще не сможет работать без двигателя, потому что у нее во всех функциях сейчас используется двигатель (motor).

my_Car = Auto()
my_Car.start()
