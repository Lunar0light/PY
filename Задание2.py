
time_s = int(input('Введите время в секундах: '))

ss = time_s % (24*3600)

hh = ss // 3600
ss %= 3600
mm = ss // 60
ss %= 60

print(f'{hh}:{mm}:{ss}')

