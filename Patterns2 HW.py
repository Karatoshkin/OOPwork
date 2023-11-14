from abc import ABC, abstractmethod

class Action(ABC):   #интерфейс
    @abstractmethod
    def Caliber(self):
        pass

    @abstractmethod
    def Type(self):
        pass

class Gun(Action):
    def Caliber(self):
        print('Caliber is: 12,7mm')

    def Type(self):
        print('This is machinegun...')

class AbsDecorator(Action):
    def __init__(self, object):
        self.object = object

    def Caliber(self):
        self.object.Caliber()

    def Type(self):
        self.object.Type()

class PDW(AbsDecorator):
    def Type(self):
        print('This is personal defence weapon...')

class Rifle(AbsDecorator):
    def Type(self):
        print('This is assault rifle ...')

class AmmoS(AbsDecorator):
    def Calibre(self):
        print('Caliber is: 0.45ACP')

class AmmoB(AbsDecorator):
    def Calibre(self):
        print('Caliber is: 5.56 NATO')


weapon = Gun()
weapon.Type()
weapon = Rifle(weapon)
weapon.Caliber()
# weapon = PDW(weapon)
# weapon.Caliber()
# weapon.Type()
