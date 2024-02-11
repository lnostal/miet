> В какой момент создается новый объект функции?

Определение функции начинается с выражения def, которое состоит из имени функции, набора параметров в скобках и двоеточия. Параметры в скобках необязательны. (???)

В момент ее вызова (?)

> Почему следует избегать модификации изменяемых аргументов?

* аргументы передаются через присваивание объектов именам локальных переменных функций

* при передаче объекты никогда не копируются автоматически

* присваивание аргументов внутри функции не затрагивает вызывающий код

* при выполнении функции аргументы функции становятся ее локальными переменными в области видимости функции

* имена аргументов функции и имена переменных в области видимости функции не совмещаются

* __модификация изменяемого объекта внутри функции может затронуть вызывающий код__

В следующем примере видно, как изменение на месте изменяемого объекта внутри функции приводит к последствиям определенного рода:

```python
    def func(a):
        print(a)
        a.append('that')
        print(a)

    a = ['this']
    func(a)
    print(a)
```
```
    ['this']
    ['this', 'that']
    ['this', 'that']
```

<!-- В Python значение аргумента по умолчанию определяется один раз во время определения функции. Затем каждый раз, когда мы вызываем функцию без аргументов, используется один и тот же изменяемый аргумент (например, список). В итоге элементы накапливаются в списке с каждым вызовом функции. -->

> Что такое интроспекция?

Способность программы исследовать тип или свойства объекта во время работы программы. Поскольку функции являются объектами, мы можем работать с ними посредством обычных инструментов для объектов.

```python
def my_fun(*, a, b, c):
    pass

my_fun.prop = "qwerty" # добавление нового атрибута функции
print(dir(my_fun)) # вывода списка атрибутов объекта
```

> Что такое аннотация функций?

Произвольные определяемые пользователем данные об аргументах и результате функции.

```python
def my_fun(a: str, b: float, c: tuple = (1, 2)) -> float:
    return len(a) + len(c) + b
 ```

> Что такое анонимная функция?

Анонимные функции могут содержать лишь одно выражение, выполняются быстрее. Cоздаются с помощью инструкции `lambda`. 

> Правило LEGB.

LEGB - Local, Enclosing, Global и Built-in Scope - типы областей видимости

* Local - определяется внутри функции и доступна только из этой функции
* Enclosing (_nonlocal_) - closure - переменная не является локальной следовательно, ее значение будет взято из ближайшей области видимости, в которой существует переменная с таким же именем
* Global - переменная определена вне любой из функций и доступна любой функции в программе
* Built-in Scope - встроенные функции (print, input, open и т.д)

Для поиска имен в Python определен следующий порядок:

`LOCAL -> ENCLOSING-> GLOBAL -> BUILT-IN:`

> Генераторные функции.

Функция, которая содержит оператор yield и возвращает объект-генератор.
Пример:

```python
def squares(length):
    for n in range(length):
        yield n ** 2
```
```python
for square in squares(5):
    print(square)
```
```
0
1
4
9
16
```


> Генераторные выражения.

Выражение, которое возвращает объект-генератор. Более простой способ (без объявления функции)

```python
squares = (n** 2 for n in range(5))

for square in squares:
    print(square)
```

Вывод аналогичен предыдущему коду.

> Что такое модуль?

Отдельный файл с кодом, который можно повторно использовать в других программах.

> Как работает поиск модуля при импортировании?

При импорте модуля, интерпретатор Python пытается найти модуль в следующих местах:
1. Директория, где находится файл, в котором вызывается команда импорта.
2. Директория, определённая в консольной переменной PYTHONPATH (если модуль не найден с первого раза).
3. Путь, заданный по умолчанию (если модуль не найден в предыдущих двух случаях). 

Что касается пути поиска, то он сохраняется в переменной path в системном модуле sys. А переменная sys.path включает в себя все 3 вышеописанных места поиска.

> Для чего нужны файлы `__init__.py`?

Пакет в Python — это способ организации пространства имен, позволяющий объединять несколько модулей в единую структуру. Чтобы позволить Python распознать директорию как пакет, в ней должен быть файл с названием `__init__.py`. Этот файл может быть пустым, или содержать код инициализации пакета. Он выполняется при импорте любого модуля из пакета.