
# В файле записаны целые числа (создайте самостоятельно). Найти
# максимальное и минимальное число и записать в другой файл

import os
import re

textFromFile = list()

with open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', "r") as file:
    content = file.read()
    textFromFile = content.replace('\n',' ').split(' ')


textFromFileWithoutEmpties = list(filter(None, textFromFile))
regexp = re.compile(r'^-?[0-9]*$')
numbers = [i for i in textFromFileWithoutEmpties if regexp.search(i)]

numbers = list(map(int, numbers))

with open(os.path.dirname(os.path.abspath(__file__)) + '/output.txt', "w") as file:
    if len(numbers) != 0:
        print("max: {0}\nmin: {1}".format(max(numbers), min(numbers)), file=file)
    else:
        print("",file=file)