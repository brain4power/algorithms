import random

m = 5
size = 2*m + 1
min_item = 0
max_item = 20
array = [random.randint(min_item, max_item) for _ in range(size)]


def median(array):
    counts = {}
    for each in array:
        if each in counts:
            counts[each] += 1
        else:
            counts[each] = 1
    for i in range(len(array)):
        less = 0
        more = 0
        for j in range(len(array)):
            if array[j] > array[i]:
                more += 1
            elif array[j] < array[i]:
                less += 1
        if abs(less - more) <= counts[array[i]]:
            return array[i]


print(sorted(array))
print(median(array))
