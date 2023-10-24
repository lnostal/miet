
# Напишите функцию, которая принимает список из целых чисел и
# возвращает кортеж только чётных чисел.

def train(nums):
    evens = list(filter(lambda x: x % 2 == 0, nums))
    return tuple(evens)

print(train([1,2,3,4,5,6,7,8])) # (2, 4, 6, 8)


