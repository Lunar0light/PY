rev = float(input('Сумма выручки - '))
cost = float(input('Сумма издержек - '))
if rev > cost :
    print('Выручка больше издержек')
    profit = (rev - cost) / rev
    print(f'Рентабельность: {profit}')
    num_emp=int(input('Количество сотрудников: '))
    rev_e_o=(rev - cost) / num_emp
    print(f'Прибыль на каждого сотрудника: {rev_e_o}')
if rev < cost :
    print('Выручка меньше издержек')
if rev == cost :
    print('Выручка равно издержекам')
