# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


def reverse(number):
    if number // 10 == 0:
        return number
    else:
        return f'{number % 10}{reverse(number // 10)}'


user_number = int(input('Введите натуральное число до 1000 знаков: '))
print(f'Обратное число: {reverse(user_number)}')
