
# Считать из файла input.txt 10 чисел (числа записаны через пробел).
# Затем записать их произведение в файл output.txt.

import os
import re

textFromFile = list()

with open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', "r") as file:
    content = file.read()
    textFromFile = content.replace('\n',' ').split(' ')

textFromFileWithoutEmpties = list(filter(None, textFromFile))

s = ' '.join(textFromFileWithoutEmpties[:10])

with open(os.path.dirname(os.path.abspath(__file__)) + '/output.txt', "w") as file:
    print(s, file=file)