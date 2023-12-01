# Задание №3
# Выполните поиск содержимого текущей директории (включая поддиректории) и
# найдите все файлы с расширением txt в которых есть ключевое слово key.
# Выполните задание в одном и в нескольких потоках.

import os
from time import perf_counter
from threading import Thread

files_txt = []
files_with_key = []

for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
#for root, dirs, files in os.walk("/Users/nosta/Documents/study"):
    for file in files:
        if file.endswith(".txt"):
             files_txt.append(os.path.join(root, file))


def findFile(filename):
    with open(filename, "r") as file:
        content = file.read()
        if "key" in content:
            files_with_key.append(filename)

def one_thread():
    for file in files_txt:
        findFile(file)


def many_threads():
    threads = []
    for file in files_txt:
        t = Thread(target=findFile, args=(file,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


start_time = perf_counter()
one_thread()
end_time = perf_counter()

files_with_key.clear()

start_time2 = perf_counter()
many_threads()
end_time2 = perf_counter()


print(f'\n\nПоследовательное выполнение заняло {end_time - start_time: 0.6f} секунд.')
print(f'Параллельное выполнение заняло {end_time2 - start_time2: 0.6f} секунд.')
