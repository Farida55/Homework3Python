from curses.ascii import isdigit
import re
from sympy import true

def sum_digits(a):
    if a.isdigit():
        return True
    else:
        return False

def Main():
    a = str(input('enter the num: '))
    s = list(filter(sum_digits, a)) ## filter
    s = [int(i) for i in s] ## list comprehension
    print(s)
    print(sum(s))
   
Main()