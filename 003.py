# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import numpy
from random import randint as r
 
list_inp = [r(-10, 30) for i in range(20)]

res = numpy.array(list_inp)
unique_res = numpy.unique(res)
print(res)
print()
print (" Unique elements of the list:\n", unique_res)