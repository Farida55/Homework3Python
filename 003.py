# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def getList(size):
    if size < 0:
        size = -size
    result = [0.0] * size
    for i in range(size):
        result[i] = round(random.uniform(0, 1000), 4)
    print(result)
    return result


def minMax(List):
    min = List[0] - List[0] // 1
    max = min
    for i in range(len(List)):
        fract = List[i] - List[i] // 1
        if fract > max:
            max = fract
        if fract < min:
            min = fract
    print('Minimum fractional part: ', round(min, 4), 'Maximum fractional part: ', round(max, 4), end=' ')
    return round(max - min, 4)


print('Difference: ',minMax(getList(int(input('Enter the size of the list: ')))))
