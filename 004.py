# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_sys_to_bin(num):
    if num == 0:
        print(num)
        return
    elif num != 1:
        dec_sys_to_bin(num // 2)
    print(num % 2, end='')


dec_sys_to_bin(int(input('Enter the decimal number: ')))
print()
