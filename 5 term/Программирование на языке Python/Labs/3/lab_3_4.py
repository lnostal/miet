
# Напишите функцию, которая принимает в качестве аргумента целое
# число от 1 до 12 и возвращает соответствующее название месяца.
# Пример: 2 => Февраль

# просто кортеж упорядоченных констант

months = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")

def getMonthById(id):
    if type(id) is int and id > 0 and id < 13:
        return months[id-1]
    else:
        return "wrong input"

print(getMonthById(6))

# можно также решить через Enum и/или библиотеки работы с датами, но в условиях текущей задачи это был бы овераркитект