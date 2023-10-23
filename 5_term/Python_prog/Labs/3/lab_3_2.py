
# Напишите функцию, которая принимает неограниченное количество
# целых чисел (в качестве аргументов) и возвращает их среднеарифметическое
# значение.

from statistics import mean

def arithmean(*nums):
    if len(nums) != 0:
        return mean(nums)

print(arithmean(1,2,3)) # 2
print(arithmean(1,2,3,4,5,6,7,8)) # 4.5
print(arithmean(11,6,0,2)) # 4.75

print(arithmean())