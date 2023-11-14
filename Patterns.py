from abc import ABC, abstractmethod


class Povedenie(ABC): #Интерфейс - управления
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Enemy(Povedenie):#Суперкласс
    def __init__(self, a, b):#Создание объекта
        self.weapon = a
        self.speed = b

    def run(self):
        print('speed:', self.speed)

    def attack(self):
        print('weapon:', self.weapon)


en1 = Enemy('Chopa', 'Middle')
en1.run()
en1.attack()


class Goblin(Enemy):
    def __init__(self):
        super().__init__('Knife', 'High')


class Troll(Enemy):
    def __init__(self):
        super().__init__('Fist', 'Low')


class Factory():
    def create(self, name):
        if name == 'goblin':
            return Goblin()
        elif name == 'troll':
            return Troll()
        else:
            return 'неизвестный тип'


myfactory = Factory()#Создали фабрику
en2 = myfactory.create('goblin')
en2.run()
en3 = myfactory.create('troll')
en3.run()
en3.attack()