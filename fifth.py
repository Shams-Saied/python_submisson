from abc import ABC, abstractmethod

class robot(ABC):
    def __init__(self,name,battery_level):
        self.__name=name
        self.__battery_level=battery_level
    
    def status(self):
        print(f"{self.__name}, Battery level: {self.__battery_level}%")

    @abstractmethod
    def move(self):
        pass
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,n):
        self.__name=n







class groundRobot(robot):
    def __init__(self,name,battery_level,wheels):
        super().__init__(name,battery_level)
        self.__wheels=wheels

    def move(self):
        print(f"{self.name} is moving on {self.__wheels} wheels.")

    @property
    def wheels(self):
        return self.__wheels
    
    @wheels.setter
    def wheels(self,w):
        self.__wheels=w

class aerialRobot(robot):
    def __init__(self,name,battery_level,rotors):
        super().__init__(name,battery_level)
        self.__rotors=rotors

    def move(self):
        print(f"{self.name} is moving on {self.__rotors} rotors.")

    @property
    def rotors(self):
        return self.__rotors
    
    @rotors.setter
    def rotors(self,r):
        self.__rotors=r

robot1=aerialRobot("one",90,4)

robot1.move()

robot1.status()

print(robot1.battery_level)