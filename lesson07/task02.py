import random
from collections import deque

size = 11
min_item = 0
max_item = 50
array = [random.random()*(max_item - min_item) + min_item for _ in range(size)]


def merge_sort(array):
    left = deque([])
    right = deque([])
    deque(array)
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    for i in range(middle):
        left.append(array[i])
    for i in range(middle, len(array)):
        right.append(array[i])
    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)
    return result


def merge(left, right):
    result = deque([])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    while len(left) > 0:
        result.append(left.popleft())
    while len(right) > 0:
        result.append(right.popleft())
    return result


print(array)
print(list(merge_sort(array)))

