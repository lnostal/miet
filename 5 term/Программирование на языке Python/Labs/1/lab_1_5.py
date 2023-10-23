# Последовательно вводятся ненулевые числа. Определить сумму
# положительных и сумму отрицательных чисел.
# Закончить ввод чисел при вводе 0.

print("Введите ненулевые числа:\n")

positiveNumsSum = 0
negativeNumsSum = 0

while True:
    strNum = input()
    try:
        num = int(strNum)

        if num == 0:
            break

        if num > 0:
            positiveNumsSum += num
        else:
            negativeNumsSum += num
    except:
        print("not number, try again")

print("сумма положительных чисел:\t {0}\nсумма отрицательных чисел:\t{1}".format(positiveNumsSum, negativeNumsSum))