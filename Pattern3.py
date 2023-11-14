
#Наблюдатель поведенческий

class CameraSystem():
    def __init__(self):
        self.observers = set()  #Здесь хранятся объекты

    def connection(self, obs):  #Добавить в список
        self.observers.add(obs)

    def disconnect(self, obs):  #Удалить из списка
        self.observers.remove(obs)

    def signal(self):   #Включить все объекты из списка
        for obs in self.observers:
            # if 'camera' in obs.name:
            #     obs.photo()
            # elif 'turrel' in obs.name:
            #     obs.fire()
            if isinstance(obs, Camera):     #Проверка что находится в классе камера
                obs.photo()
            elif isinstance(obs, Turrel):       #Проверка что находится в классе турель
                obs.fire()

from abc import ABC, abstractmethod

class PovedenieCam(ABC):
    @abstractmethod
    def photo(self):
        pass


class Camera(PovedenieCam):
    def __init__(self, name):
        self.name = name

    def photo(self):
        print(self.name, 'took a photo')

class PovedenieTur(ABC):
    @abstractmethod
    def fire(self):
        pass

class Turrel(PovedenieTur):
    def __init__(self, name):
        self.name = name
    def fire(self):
        print(self.name, 'battleTurrels - activated!')

CamSys = CameraSystem()     #Создаем систему
cam1 = Camera("camera1")    #Создаем объекты
cam2 = Camera("camera2")
cam3 = Camera("camera3")
tur1 = Turrel("turrel1")
tur2 = Turrel("turrel2")
CamSys.connection(cam1)     #Подключение объектов к системе
CamSys.connection(cam2)
CamSys.connection(cam3)
CamSys.connection(tur1)
CamSys.connection(tur2)
CamSys.signal()            #Все объекты начинают работать