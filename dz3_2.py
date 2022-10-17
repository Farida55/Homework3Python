from random import randint as r
 
list_inp = [r(-10, 30) for i in range(20)] ## list comprehension
print(list_inp)
new_list = [x for i, x in enumerate(list_inp) if i == list_inp.index(x)] ## enumerate
print(new_list)

