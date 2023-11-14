class Ship():
    def move(self):
        self.distance += 10

    def port(self):
        print('Иду в порт')

    def anchor(self):
        print('Отдать якорь!')

    def __init__(self):
        self.distance = 0
        self.speed = 20

class Frigate(Ship):
    def move(self):
        self.distance += 16


    def __init__(self, quantitygun=20,type='Фрегат'):
        self.quantitygun = quantitygun
        self.type=type
        self.distance = 1
        self.speed = 30

    def fire(self):
        print(self.type, 'стреляет из', self.quantitygun, 'пушек')

class Yacht(Ship):
    def move(self):
        self.distance += 12.3

    def __init__(self, quantitygun=2,type='Яхта'):
        self.quantitygun = quantitygun
        self.type = type
        self.distance = 0
        self.speed = 17.1

    def fire(self):
        print(self.type, 'стреляет из', self.quantitygun, 'пушек')


freg = Frigate()
for i in range(5):
    print(i + 1, freg.distance)
    freg.move()
freg.fire()
yaht = Yacht()
for i in range(5):
    print(i + 1, yaht.distance)
    yaht.move()
yaht.fire()



