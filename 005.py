# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def lineCountInFile(path):
    file = open(path, 'r')
    lines = 0
    for line in file:
        if line != "\n":
            lines += 1
    return lines


def mergeLinesInFles(path1, path2):
    if lineCountInFile(path1) != lineCountInFile(path2):
        print('The contents of the files do not match!')
        return
    poly1 = open(path1, 'r')
    poly2 = open(path2, 'r')
    with open('polySum.txt', 'w') as result:
        for i in range(lineCountInFile(path1)):
            result.write(poly1.readline().replace('=0\n', '+') +
                         poly2.readline())

    poly1.close()
    poly2.close()


path1 = 'poly1.txt'
path2 = 'poly2.txt'

mergeLinesInFles(path1, path2)
