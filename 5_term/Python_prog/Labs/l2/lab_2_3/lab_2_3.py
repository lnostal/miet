
# Даны два текстовых файла (input_1.txt, input_2.txt), необходимо
# записать в файл output.txt все слова, которые встречаются в обоих файлах.

import os
import string
import numpy


def openFile(fileName):
    with open(os.path.dirname(os.path.abspath(__file__)) + fileName, "r") as file:
        return file.read()
    
def getAllWords(text):
    t = text.replace('\n', ' ')
    blacklist = string.punctuation + '—'
    new_s = ''.join(char for char in t if char not in blacklist)

    return new_s.split(' ')

def getDataFromFile(file):
    data = openFile(file)
    return getAllWords(data)


listOfWords_1 = getDataFromFile('/input_1.txt')
listOfWords_2 = getDataFromFile('/input_2.txt')

repeated = numpy.intersect1d(listOfWords_1, listOfWords_2)
repStr = ' '.join(repeated)

with open(os.path.dirname(os.path.abspath(__file__)) + '/output.txt', "w") as file:
        print(repStr,file=file)

