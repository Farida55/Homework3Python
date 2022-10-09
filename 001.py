# Вычислить число c заданной точностью d
# *Пример:*
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

digit = Decimal(input('Enter a real number: '))
digit = digit.quantize(Decimal(input('Enter the required accuracy "0.0001":')))
print(digit)