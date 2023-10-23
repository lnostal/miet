
# Пользователь с клавиатуры вводит имя и отчество, необходимо
# вывести на экран инициалы.
# Пример: Иван Сергеевич – И.С.

import re

fio = input("Введите имя и отчество:\n")

separatedFio = fio.split(" ")

initials = ""

regexp = re.compile(r'[0-9]')

if len(separatedFio) != 2 or regexp.search(fio):
    print("wrong input")
else:
    for s in separatedFio:
        initials += s[0] + ". "

    print(initials.upper())