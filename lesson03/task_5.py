# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

size = 10
min_item = -100
max_item = 80
array = [random.randint(min_item, max_item) for _ in range(size)]

max_number = min_item - 1
idx_number = 0
for idx, element in enumerate(array):
    if element < 0:
        if element > max_number:
            max_number = element
            idx_number = idx

print(f'array: {array}')
if max_number != min_item - 1:
    print(f'Максимальный отрицательный элемент в массиве: {max_number} на позиции {idx_number + 1}')
else:
    print(f'В массиве нет отрицательных элементов')
