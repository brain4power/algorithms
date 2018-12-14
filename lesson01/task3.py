print('у1-у2 и х2-х1 не должны быть одновременно равны нулю')
x1 = int(input('Введите х1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите х2: '))
y2 = int(input('Введите y2: '))
if y1 - y2 == 0:
    if x1*y2 == x2*y1:
        print('Уравнение прямой: {}y = 0'.format(x2 - x1))
    else:
        print('Уравнение прямой: {}y = {}'.format(x2 - x1, -1*(x1*y2 - x2*y1)))
else:
    if x2 - x1 == 0:
        if x1*y2 == x2*y1:
            print('Уравнение прямой: {}x = 0'.format(y1 - y2))
        else:
            print('Уравнение прямой: {}x = {}'.format(y1 - y2, -1*(x1*y2 - x2*y1)))
    else:
        if x2 - x1 < 0:
            print('Уравнение прямой: {}x {}y = {}'.format(y1 - y2, x2 - x1, -1*(x1*y2 - x2*y1)))
        else:
            print('Уравнение прямой: {}x + {}y = {}'.format(y1 - y2, x2 - x1, -1*(x1*y2 - x2*y1)))
