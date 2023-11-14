from abc import ABC, abstractmethod


class Car(ABC): #Интерфейс - управления
    @abstractmethod
    def Country(self):
        pass

    @abstractmethod
    def Brand(self):
        pass

    @abstractmethod
    def Name(self):
        pass

    @abstractmethod
    def BodyType(self):
        pass

    @abstractmethod
    def Color(self):
        pass

    @abstractmethod
    def Engine(self):
        pass

    @abstractmethod
    def Drive(self):
        pass

# class Povedenie2(ABC):
#     @abstractmethod
#     def run(self):
#         pass


class Usercar(Car):#Суперкласс
    def __init__(self, a, b, c, d, e, f, g):#Создание объекта
        self.country = a
        self.brand = b
        self.name = c
        self.bodytype = d
        self.color = e
        self.engine = f
        self.drive = g

    def Country(self):
        print('Страна производитель:', self.country)

    def Brand(self):
        print('Марка:', self.brand)

    def Name(self):
        print('Модель:', self.name)

    def BodyType(self):
        print('Кузов:', self.bodytype)

    def Color(self):
        print('Цвет:', self.color)

    def Engine(self):
        print('Двигатель:', self.engine)

    def Drive(self):
        print('Привод', self.drive)


en1 = Usercar('Japan', 'Mitsubishi', 'Libero', 'Wagon', 'White', 'I2.0', '4WD')
# en1.Country()
# en1.Brand()
# en1.Name()
# en1.BodyType()
# en1.Color()
# en1.Engine()
# en1.Drive()


class Car1(Usercar):
    def __init__(self):
        super().__init__('Japan', 'Nissan', 'Liberty', 'Wagon', 'White', 'I1.6T', 'AWD')
class Car2(Usercar):
    def __init__(self):
        super().__init__('Japan', 'Mitsubishi', 'Libero', 'Wagon', 'White', 'I2.0', '4WD')
class Car3(Usercar):
    def __init__(self):
        super().__init__('Korea', 'KIA', 'Sorento', 'Crossover', 'Blacksea', 'I2.0', 'AWD')
class Car4(Usercar):
    def __init__(self):
        super().__init__('Japan', 'Subaru', 'Forester', 'Wagon', 'Silver', 'I3.0', '4WD')

class Factory():
    def create(self, name):
        if name == 'Nissan':
            return Car1()
        elif name == 'Mitsubishi':
            return Car2()
        elif name == 'KIA':
            return Car3()
        elif name == 'Subaru':
            return Car4()
        else:
            return 'неизвестный тип'


myfactory = Factory()#Создали фабрику
en2 = myfactory.create('Mitsubishi')
en2.Name()
en2.Brand()
