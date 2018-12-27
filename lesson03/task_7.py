# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

size = 10
min_item = 1
max_item = 30
array = [random.randint(min_item, max_item) for _ in range(size)]

print(f'array: {array}')

first_min, second_min = max_item + 1, max_item + 1

for element in array:
    if element < first_min:
        first_min, second_min = element, first_min
    elif element < second_min:
        second_min = element

print(f'Певый наименьший элемент: {first_min}, второй: {second_min}')
