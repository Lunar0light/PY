#не разобрался что приходит в other
class Cell:
    def __init__(self, num_el_cell):
        self.n=num_el_cell #количество ячеек в клетке
    def __add__(self, other):
        self.n_oth= other
        return self.n_oth + self.n

    def __sub__(self, other):
        self.n_oth = (other)
        #print(other)
        #a = self.n_oth - self.n
        #print(a)
       # if a < 0:
       #     print('total cell < 0')
      #  if a >= 0:
        return self.n_oth - self.n #почему-то не работает если из n вычитать n_oth



    def __mul__(self, other):
        self.n_oth = other
        return  self.n_oth * self.n

    def __truediv__(self, other):
        self.n_oth = str(other)
        return   self.n // self.n_oth #не поддерживаемые операнды для классов Cell

    def make_order(self):


c1=Cell(5)
c2=Cell(10)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1//c2)