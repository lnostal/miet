
# Дан текстовый файл input.txt. Определить частоту повторяемости
# каждой кириллической буквы в тексте, отсортировать в порядке убывания частоты,
# результат записать в файл output.txt. Продемонстрировать работу алгоритма на
# файлах различной длины.

# TODO: переписать алгоритм на построчное считывание, т.к. считывание 
#       всего файла в память может привести к переполнению оной

import os
import sys

def openFile(fileName):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + fileName, "r") as file:
        return file.read()
    
def writeToFile(fileName, data):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + fileName, "w") as file:
        print(data,file=file)

whitelist = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def prepareData(text):
    new_s = ''.join(char for char in text if char in whitelist)
    return new_s

def analyzeData(text):
    data = prepareData(text.lower())
    rate = {}

    for letter in whitelist:
        rate[letter] = data.count(letter)

    rate = sorted(rate.items(), key=lambda x:x[1], reverse=True)

    return rate


def main():
    if len(sys.argv) != 2:
        print("usage: \nlab_2_4.py [filename]")
        return

    fileName = sys.argv[1]

    data = openFile(fileName)
    rate = analyzeData(data)

    writeToFile('output.txt', rate)

main()