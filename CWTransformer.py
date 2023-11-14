class Transformer(): #Абстракция!!!!!!! Выбираем конкретные действия для робота (Бегать и заправляться)
    def run(self):
        if self.fuel<=0:
            print('Warning!Out of fuel!')
        else:
            self.dist+=10
            self.fuel-=1

    def zapravka(self):
        self.fuel+=10
        print('Refuel', self.diesel)

    def __init__(self):
        self.dist=0
        self.fuel=10
        self.diesel="дизель" # Public
        self._dance='gopak'# _ - защищенный способ. Protected
        self.__jump = 'visoko' # __ - Private

    def onjump(self):
        return self.__jump # Инкапсуляция. Способ запуска защищенного файла.


Fedor = Transformer()
print(Fedor._dance)
print(Fedor.onjump())
print(Fedor.dist, Fedor.fuel)
Fedor.run()
print(Fedor.dist, Fedor.fuel)
print('#################################################')
mark = Transformer()
for i in range(30):
    print(i+1, mark.dist)
    mark.run()
print('#################################################')

class Autobot(Transformer): #Наследование. Потомок обладает свойствами и методами родителя автоматом.
    def run(self):
        if self.fuel<=0:
            print("Warning!Out of fuel!")
            self.zapravka()
        else:
            self.dist+=100
            self.fuel-=1

    def __init__(self, type='auto'):
        Transformer.__init__(self)
        self.model = 'Robot'
        self.type = type
        self.dist = 0
        self.fuel = 10
        self.diesel = "дизель"

    def transform(self):
        if self.model!='Robot':
            self.model='Robot'
        else:
            self.model = self.type
        print('Transform process into ...', self.model)
        print('Transform complete!')

class Desepticon(Transformer):
    def run(self):
        if self.fuel<=0:
            print("Warning!Out of fuel!")
            self.zapravka()
        else:
            self.dist += 200
            self.fuel -= 2

    def __init__(self, type='Combat aircraft'):
        Transformer.__init__(self)
        self.model = 'Robot'
        self.type = type
        self.dist = 0
        self.fuel = 10
        self.diesel = "дизель"

    def transform(self):
        if self.model!='Robot':
            self.model='Robot'
        else:
            self.model = self.type
        print('Transform process into ...', self.model)
        print('Transform complete!')


optim = Autobot('Truck')
optim.run()
print(optim.dist, optim.fuel)
optim.transform() #Полиморфизм. Автобот становиться автомобилем и обратно роботом.
optim.transform()
optim.transform()


mega = Desepticon()
mega.run()
print(mega.dist, mega.fuel)
mega.transform()
mega.transform()
mega.transform()

