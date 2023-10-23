
# Пользователь с клавиатуры вводит произвольную строку,
# необходимо выведите на экран YES, если все символы находятся в верхнем
# регистре и NO – в противном случае.


analyzedString = input("Введите строку:\n")

try:
    int(analyzedString)
    print("not string")

except ValueError:
    if analyzedString == "":
        print("empty string")
    elif analyzedString == analyzedString.upper():
        print("YES")
    else:
        print("NO")
