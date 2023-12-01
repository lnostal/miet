# Задание №2
# Получите содержимое 10 сайтов. Выполните задание в одном и в нескольких
# потоках. Сравните результаты и время выполнения программы.

urls = [
    "https://www.google.com/",
    "https://dzen.ru/",
    "https://music.youtube.com/",
    "https://youtube.com/",
    "https://music.yandex.ru/",
    "https://myfuturama.top/",
    "https://github.com/",
    "https://web.whatsapp.com/",
    "https://docs.python.org/3/",
    "https://miro.com/ru/"
]

from urllib.request import urlopen
from time import perf_counter
from threading import Thread
import certifi

def task(url, id):
    print(f'\nНачинаем выполнение задачи {id} {url}...')
    try:
        u = urlopen(url, cafile=certifi.where())
        mysite = u.read()    
        print(f'Задача {id} выполнена')
    except:
        print("Ошибка при загрузке", url)


def one_thread():
    x = 0;
    for url in urls:
        x+=1
        task(url,x)

        
def many_threads():
    threads = []
    for n in range(1, 11):
        t = Thread(target=task, args=(urls[n-1],n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


start_time = perf_counter()
one_thread()
end_time = perf_counter()

start_time2 = perf_counter()
many_threads()
end_time2 = perf_counter()



print(f'\n\nПоследовательное выполнение заняло {end_time - start_time: 0.2f} секунд.')
print(f'Параллельное выполнение заняло {end_time2 - start_time2: 0.2f} секунд.')
