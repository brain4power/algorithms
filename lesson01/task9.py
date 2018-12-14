print('Введите три разных числа.')
first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
third = float(input('Введите третье число: '))
if first > second:
    if third > first:
        print('Первое число среднее.')
    elif third < second:
        print('Второе число среднее.')
    else:
        print('Третье число среднее.')
elif third > second:
    print('Второе число среднее.')
elif third < first:
    print('Первое число среднее.')
else:
    print('Третье число среднее.')
