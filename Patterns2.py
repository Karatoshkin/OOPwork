#Декаратор (структурный паттерн)

from abc import ABC, abstractmethod

class Povedenie(ABC):   #интерфейс
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Animal(Povedenie):
    def move(self):
        print('Move')

    def eat(self):
        print('Favorite food:')

class AbsDecorator(Povedenie):
    def __init__(self, object):
        self.object = object

    def move(self):
        self.object.move()

    def eat(self):
        self.object.eat()

class Swim(AbsDecorator):
    def move(self):
        print('Im swim')

class Fly(AbsDecorator):
    def move(self):
        print('Im fly')

class Predator(AbsDecorator):
    def eat(self):
        print('Eat meat')

class Grass(AbsDecorator):
    def eat(self):
        print('Eat grass')

ani = Animal()
ani.eat()
ani = Fly(ani)
ani.move()
ani = Predator(ani)
ani.move()
ani.eat()
