
# Пользователь с клавиатуры вводит N целых чисел, необходимо
# вывести на экран только уникальные числа (не повторяющиеся).

analyzedString = input("Введите числа: \n")

arr = analyzedString.split(" ")

onlyNumbers = []

for n in arr:
    try: 
        onlyNumbers.append(int(n))
    except ValueError:
        continue

print("list:\t", onlyNumbers)

setOfNumbers = set(onlyNumbers)

print("set:\t", setOfNumbers)