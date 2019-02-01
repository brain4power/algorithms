import random

size = 10
min_item = -100
max_item = 99
array = [random.randint(min_item, max_item) for _ in range(size)]


def bubble(array):
    n = 1
    flag = True
    while n < len(array) and flag:
        flag = False
        for i in range(n, len(array))[::-1]:
            if array[i] > array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                flag = True
        n += 1
    return array


print(f'Исходный массив: {array}')
print(f'Отсотрированный массив: {bubble(array)}')
