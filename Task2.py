from abc import ABC, abstractmethod
class Wear:
    def __init__(self):
        self.total_cons=0
        #print(f'total= {self.total_cons}') если активировать здесь, можно посчитать
        #расход на всю одежду одного экземпляра


    @abstractmethod  #наследовать не пришлось
    def costume(self, h):
        self.consumption_h=2*h+0.3
        self.total_cons= self.total_cons + self.consumption_h
        print(f'cons={self.consumption_h}')


    def coat(self, v):
        self.consumption_v = v/6.5+0.5
        self.total_cons = self.total_cons + self.consumption_v
        print(f'cons={self.consumption_v}')

    def total(self):
        print(f'total= {self.total_cons}')




m = Wear()
m.coat(1)
m.costume(10)

m2=Wear()
m2.coat(9)
m2.costume(1)

m2.total() #общий расход можно вызвать любым экземпляром класса

