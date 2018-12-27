# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]

print(f'old array: {array}')
min_idx, max_idx = 0, 0
min_number, max_number = array[0], array[0]
for idx, element in enumerate(array):
    if element > max_number:
        max_number = element
        max_idx = idx
    if element < min_number:
        min_number = element
        min_idx = idx

array[min_idx], array[max_idx] = array[max_idx], array[min_idx]
print(f'new array: {array}')
