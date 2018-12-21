# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_of_digits(number):
    summary = 0
    for i in number:
        summary += int(i)
    return summary


max_number = 0
max_summary = 0
choice = 'y'
while choice == 'y':
    user_number = str(input('Введите натуральное число: '))
    if sum_of_digits(user_number) > max_summary:
        max_summary = sum_of_digits(user_number)
        max_number = user_number
    choice = str(input('Введем еще число? y/n: '))
print('Максимальная сумма цифр: {}'.format(max_summary))
print('Соответствующее число: {}'.format(max_number))
