class Gun():
    def __init__(self, boep='50mm', color='haki', dist=1000):
        self.ammo=25

    def fire(self):
        if self.ammo:
            print('fire')
            self.ammo-=1
        else:
            print('empty')

    def reload(self):
        print("reload")
        self.ammo=25

gun1=Gun()
gun2=Gun(boep='20mm', color='pink', dist=250)
for i in range(26):
    gun1.fire()
gun1.reload()

class Transformer():
    def __init__(self, leftgun, rigthgun):
        self.myleft=leftgun
        self.myright=rigthgun

    def fire(self):
        self.myleft.fire()
        self.myright.fire()

robot = Transformer(gun1, gun2)
robot.fire()
print(robot.myleft.ammo)
print(gun1.ammo)
