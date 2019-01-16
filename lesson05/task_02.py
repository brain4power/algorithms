from collections import deque


def add_my(first_number, second_number):
    if len(first_number) - len(second_number) < 0:
        first_number, second_number = second_number, first_number
    first_number = deque(first_number)
    second_number = deque(second_number)
    first_number.reverse()
    second_number.reverse()
    for i in range(len(first_number) - len(second_number)):
        second_number.append('0')
    sixt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
    summ = deque(['0']*len(first_number))

    def my_summ(*args, indx):
        summary = sum(args)
        if summary < 16:
            return [key for key in sixt if sixt[key] == summary][0]
        else:
            return [[key for key in sixt if sixt[key] == summary % 16][0], my_summ(summary // 16, indx=indx + 1)]

    for idx, element in enumerate(first_number):
        for in_idx, each in enumerate(my_summ(sixt[element], sixt[second_number[idx]], sixt[summ[idx]], indx=idx)):
            try:
                summ[idx + in_idx] = each
            except IndexError:
                summ.append(each)
    summ.reverse()
    return list(summ)


def my_multiply(first_number, second_number):
    if len(first_number) - len(second_number) < 0:
        first_number, second_number = second_number, first_number
    first_number = deque(first_number)
    second_number = deque(second_number)
    second_number.reverse()
    sixt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
    multiply_result = deque(['0']*len(first_number))

    def multiply_digit(first, second):
        result_mul_digit = deque(['0']*len(first))
        for i in range(sixt[second]):
            result_mul_digit = add_my(result_mul_digit, first)
        return result_mul_digit

    kr = 0
    for each in second_number:
        addend = multiply_digit(first_number, each)
        for j in range(kr):
            addend.append('0')
        kr += 1
        multiply_result = add_my(multiply_result, addend)
    return multiply_result


def beauty_output(array):
    return ''.join(array)


print(add_my('A2', 'C4F'))
print(my_multiply('A2', 'C4F'))
print(beauty_output(my_multiply('A2', 'C4F')))
