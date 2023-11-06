
# Напишите функцию, которая принимает неограниченное количество
# целых чисел (в качестве аргументов) и возвращает их среднеарифметическое
# значение.

from statistics import mean
from functools import reduce

# решение через reduce
def arth(*nums):
    if len(nums) != 0:
        sum = reduce(lambda x, y: x + y, nums)
        return sum / len(nums)

# решение через модуль statistics
def arithmean(*nums):
    if len(nums) != 0:
        return mean(nums)


print(arithmean(1,2,3,4,5,6,7,8)) # 4.5
print(arithmean()) # None

print(arth(1,2,3,4,5,6,7,8)) # 4.5
print(arth()) # None