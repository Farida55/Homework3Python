# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

path_file = input('Enter the name of the source file: ')
path_encode = input('Enter filename for RLE encoding: ')

def RLE_coding(path_file, path_encode):
    with open(path_file, 'r', encoding='utf-8') as my_f1:
        lines = my_f1.readlines()
        for line in lines:
            for_coding = line.strip()
            with open(path_encode, 'a', encoding='utf-8') as my_f2:
                i = 0
                encode = ''
                while i < len(for_coding):
                    count = 1
                    while i + 1 < len(for_coding) and for_coding[i] == for_coding[i + 1]:
                        count += 1
                        i += 1
                    encode += str(count) + for_coding[i]
                    i += 1
                for i in range(len(encode)):
                    my_f2.write(f'{encode[i]}')
                my_f2.write('\n')

def RLE_decoding(path_encode):
    decode = ''
    count = ''
    with open(path_encode, 'r', encoding='utf-8') as my_f1:
        lines = my_f1.readlines()
        for line in lines:
            for_decoding = line.strip()
            for char in for_decoding:
                if char.isdigit():
                    count += char
                else:
                    decode += char * int(count)
                    count = ''
            print(decode)
            decode = ''


RLE_coding(path_file, path_encode)
RLE_decoding(path_encode)
