#пример использования @property
class Wear:
    def __init__(self,h):
        self.h=h

    @property
    def costume(self):
        self.consumption_h=2*self.h+0.3
        print(f'cons={self.consumption_h}')


m = Wear(5)
m.costume