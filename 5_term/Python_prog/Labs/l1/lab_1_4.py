
# Напишите скрипт, который по введенному году выводит
# сообщение о том, является ли год високосным.


def checkIfLeap(year):

    if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 400 == 0:
        print("это високосный год")
    else:
        print("это обычный год")

    return

yearString = input("Введите год:\n")

try:
    checkIfLeap(int(yearString))
except:
    print("wrong input")



    