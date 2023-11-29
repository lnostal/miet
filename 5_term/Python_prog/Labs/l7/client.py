
# Скрипт, который принимает от пользователя email-адрес и текст
# сообщения (ввод данных через клавиатуру), отправляет данную
# информацию (используя сокеты) на сервер (server.py). Если сервер
# отвечает «OK», то скрипт завершает работу, иначе выводит
# пользователю информацию об ошибке и предлагает ввести данные
# заново. 

import socket

HOST = '127.0.0.1'
PORT = 50007

while(True):
    email = input("Введите e-mail: ")
    message = input("Введите текст письма: ")
    data = "{}\n{}".format(email, message)

    print("Отправляем данные...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.sendall(str.encode(data))

            data = s.recv(1024).decode()
            print(data)

            if data == "OK":
                break
        except ConnectionRefusedError as err:
            print(err)