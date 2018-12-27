# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = 10
min_item = 1
max_item = 10
array = [random.randint(min_item, max_item) for _ in range(size)]

print(f'array: {array}')

min_idx, max_idx = 0, 0
min_number = array[0]
max_number = array[0]
summary = 0

for idx, element in enumerate(array):
    if element < min_number:
        min_number = element
        min_idx = idx
    if element > max_number:
        max_number = element
        max_idx = idx

if max_idx > min_idx:
    for i in range(min_idx + 1, max_idx):
        summary += array[i]
else:
    for i in range(max_idx + 1, min_idx):
        summary += array[i]

print(f'Сумма между макс и мин элементами массива равна {summary}')
