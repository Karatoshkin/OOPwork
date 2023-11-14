from abc import ABC, abstractmethod

class Iweapon(ABC):
    @abstractmethod
    def fire(self):
        print('int')
        pass

class Rocket(Iweapon):
    def fire(self):
        print('ракета пошла')

class Laser(Iweapon):
    def fire(self):
        print('лазерное облучение')

class Ienergy(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def load(self):
        pass

class Atom(Ienergy):
    def generate(self):
        print('работает реактор')

    def load(self):
        print('заправиться ураном')

class Diesel(Ienergy):
    def generate(self):
        print("работает двигатель")
    def load(self):
        print('заправился дизелем')

class Transformer():
    def installGun(self,gun):
        self.mygun = gun

    def installEnergy(self,enr):
        self.myenergy = enr

fedor = Transformer()
gun1 = Laser()
fedor.installGun(gun1)
reactor1 = Diesel()
fedor.installEnergy(reactor1)
fedor.mygun.fire()
fedor.myenergy.load()

class Factory():
    def constructRA(self):
        robot = Transformer()
        gun = Rocket()
        reactor = Atom()
        robot.installGun(gun)
        robot.installEnergy(reactor)
        return robot

myfactory = Factory()
mega = myfactory.constructRA()
mega.mygun.fire()
