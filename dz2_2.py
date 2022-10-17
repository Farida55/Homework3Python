from itertools import accumulate

n = int(input("Enter the number "))
n = [x for x in range(1,n)] ## list comprehension
n = map(lambda x: max(x,1), n) ## map, lamba
print("The factorial of ", list(accumulate(n, lambda x, y: x * y)))
