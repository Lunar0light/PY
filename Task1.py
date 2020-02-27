class Matrix:
    def __init__(self, a):
        self.f1 = a
 #       print(self.f1[1])  сюда закидывается список,из которого можно взять элемент
   # def __add__(self, other): здесь из other уже нельзя взять элемент, хотя при печати это обычный список
   #     self.other= other
    #    print(self.other[2])
    #    for j in range(0,3):
    #        self.ad1 = str(self.f1[j])
     #       self.ad2 = str(self.other[j])
     #       self.f_2 = list(map(lambda c, d: c + d, self.ad1, self.ad2))

      #      print(self.f_2)

    def __str__(self):
        for i in range(0,3):
            self.f_1 = str(self.f1[i])
            print(f'{self.f_1}')
        return  ' '

my_l1=[1, 2, 3]
my_l2=[4, 5, 6]
my_l3=[7, 8, 9]
my_matr=[my_l1, my_l2, my_l3]

my_l11=[1, 2, 3]
my_l22=[4, 5, 6]
my_l33=[7, 8, 9]
my_matr1=[my_l11, my_l22, my_l33]

m1 = Matrix(my_matr)
m2 = Matrix(my_matr1)
print(m1) #переопределение __str__
#print(m1 + m2)
