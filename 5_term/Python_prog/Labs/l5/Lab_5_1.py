import os.path
import sys
import pickle
import codecs

# В качестве базовой программы используйте наработки из предыдущей

# directory reach
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(directory)

#import book
from l4.book_pk import book as b

# Добавьте пользовательское исключение.
class NotMenuUnit(Exception):
    pass

# Добавьте пользовательский ввод данных с клавиатуры.
# Добавьте обработку исключений на случай некорректных данных.
def validateMenuInput():
    type = input()
    typeNum = 0
    try:
        typeNum = int(type)
        if typeNum < 1 or typeNum > 4:
            raise NotMenuUnit("Not menu unit. Try again")
    except ValueError:
        print('Wrong input. Try again')
    except NotMenuUnit as e:
        typeNum = 0
        print(e)
    finally:
        return typeNum

def menu():
    print('\nSelect book type by number:')
    print('{0} [{1}] | {2} [{3}] | {4} [{5}] | {6} [{7}]'.format(b.BookType.Classic.name, b.BookType.Classic.value,
                                                                 b.BookType.Audio.name, b.BookType.Audio.value,
                                                                 b.BookType.ForeignClassic.name, b.BookType.ForeignClassic.value,
                                                                 b.BookType.ForeignAudio.name, b.BookType.ForeignAudio.value))
    selectedType = 0
    while(selectedType == 0):
        selectedType = validateMenuInput()

    return selectedType

def getDataByBookType(type):
    match type:
        case b.BookType.Classic:
            return b.Book("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600)
        case b.BookType.Audio:
            return b.AudioBook("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600, "Д. Пучков")
        case b.BookType.ForeignClassic:
            return b.ForeignBook("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600, "Р.Райт-Ковалева")
        case b.BookType.ForeignAudio:
            return b.ForeignAudioBook("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600, "Д. Пучков", "Р.Райт-Ковалева")


selectedType = menu()
print('Current book type: {}'.format(b.BookType(selectedType).name))

print

data = getDataByBookType(b.BookType(selectedType))

# Добавьте возможность сохранять и восстанавливать данные из файла (бинарная запись).
# Добавьте обработку исключений при чтении и записи файла.

def openFile(fileName):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + fileName, "rb") as file:
        return pickle.load(file)
    
def writeToFile(fileName, data):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + fileName, "wb") as file:
        pickle.dump(data, file)

writeToFile('output.pk', data)
r = openFile('output.pk')



#### todo: сделать выбор: загрузить из файла или че
####       сделать выбор сохранить или че