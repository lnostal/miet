
# Скрипт, который «слушает» сообщения от client.py. При
# получении email пользователя скрипт отправляет текст сообщения
# на email пользователя;
# В случае ошибки возвращает client.py соответствующую
# информацию, иначе отправляет «OK».

import socket
import mail

HOST = '127.0.0.1'
PORT = 50007

def parseData(data):
    i = data.find("\n")
    email = data[:i]
    msg = data[i+1:]
    return email, msg

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('Подключено: ', addr)
        data = conn.recv(1024).decode()
        print("Получены данные от клиента")
        email, msg = parseData(data)
        if not mail.valid(email):
                conn.sendall(b'Email is not valid. Try again')
                print("Ошибка в данных")
        else:
                print("Данные корректны. Отправляем письмо...")
                mail.send_message(msg)
                conn.sendall(b'OK')
                print("ОК")
                break


