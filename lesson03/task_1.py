# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

multi = {}
for i in range(2, 10):
    multi[i] = 0

for i in range(2, 100):
    for element in multi:
        if i % element == 0:
            multi[element] += 1

for element in multi:
    print('Кратны {} всего {} чисел'.format(element, multi[element]))
