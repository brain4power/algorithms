number = int(input("Введите трехзначное число: "))
mul = number % 10
summary = mul
number = number // 10
mul *= number % 10
summary += number % 10
number = number // 10
mul *= number
summary += number
print('сумма цифр равна {}'.format(summary))
print('произведение цифр равно {}'.format(mul))