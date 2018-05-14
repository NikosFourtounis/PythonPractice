__author__ = "NFourtounis"
__date__ = "$May 14, 2018 7:42:00 PM$"
from datetime import datetime
class Pet(object):
    def __init__(self,name,breed,area):
        self.name=name
        self.breed=breed
        self.area=area
        print('Created',self.name,', ',self.breed,', ',self.area)
    def getName(self):
        return self.name
    def getBreed(self):
        return self.breed
    def getArea(self):
        return self.area
    def __str__(self):
        print('bla bla bla')

if __name__ == "__main__":
    a1 = Pet('Doge','Doggoo','Greece')
    print(a1.getName())
    print(a1.getBreed())
    print(a1.getArea())
    print(a1.__str__())
    