
# Считать из файла input.txt 10 чисел (числа записаны через пробел).
# Затем записать их произведение в файл output.txt.

import os
import re
import numpy

textFromFile = []

with open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', "r") as file:
    content = file.read()
    textFromFile = content.replace('\n',' ').split(' ')

regexp = re.compile(r'^-?[0-9].?[0-9]*?$')
numbers = [float(i) for i in textFromFile if regexp.search(i)]

m = 0.0;

if len(numbers) != 0:
    m = numpy.prod(numbers[:10])

with open(os.path.dirname(os.path.abspath(__file__)) + '/output.txt', "w") as file:
    print(m, file=file)