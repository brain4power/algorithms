# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 30) for _ in range(5)] for _ in range(3)]

for line in matrix:
    print(line)

min_column = matrix[0]
for i in range(1, len(matrix)):
    for idx, element in enumerate(matrix[i]):
        if element < min_column[idx]:
            min_column[idx] = element

max_element = min_column.pop()
for element in min_column:
    if element > max_element:
        max_element = element

print(f'Максимальный элемент среди минимальных: {max_element}')
