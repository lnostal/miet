> Что такое наследование?

Наследование позволяет создавать новый класс на основе уже существующего класса. Ключевыми понятиями наследования являются подкласс и суперкласс. Подкласс наследует от суперкласса все публичные атрибуты и методы. Суперкласс еще называется базовым `(base class)` или родительским `(parent class)`, а подкласс – производным `(derived class)` или дочерним `(child class)`.

> Что такое композиция?

Когда один класс не может существовать без другого класса. Например, есть классы `A` и `B`. В случае композиции экземпляр класса `B` создается только внутри класса `A` и управляется им же. 

> Аннотация свойств.

`@property / @%name%.setter`

свойство `@property` ставится на месте обычного поля с сохранением имени. Таким образом сохраняется интерфейс класса, но при этом можно навесить дополнительную логику на операции чтения / записи поля

> Для чего нужен метод `__str__()`?

для человекопонятного вывода описания класса в консоль