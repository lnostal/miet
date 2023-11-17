import os.path
import sys
import pickle

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
def validateSelectBookTypeMenuInput():
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

def selectBookTypeMenu():
    print('\nSelect book type by number:')
    print('{0} [{1}] | {2} [{3}] | {4} [{5}] | {6} [{7}]'.format(b.BookType.Classic.name, b.BookType.Classic.value,
                                                                 b.BookType.Audio.name, b.BookType.Audio.value,
                                                                 b.BookType.ForeignClassic.name, b.BookType.ForeignClassic.value,
                                                                 b.BookType.ForeignAudio.name, b.BookType.ForeignAudio.value))
    selectedType = 0
    while(selectedType == 0):
        selectedType = validateSelectBookTypeMenuInput()

    return selectedType

def getDataByBookType(i):
    type = b.BookType(i)

    match type:
        case b.BookType.Classic:
            return b.Book("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600)
        case b.BookType.Audio:
            return b.AudioBook("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600, "Д. Пучков")
        case b.BookType.ForeignClassic:
            return b.ForeignBook("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600, "Р.Райт-Ковалева")
        case b.BookType.ForeignAudio:
            return b.ForeignAudioBook("Колыбель для кошки", "Курт Воннегут", "АСТ", 250, 600, "Д. Пучков", "Р.Райт-Ковалева")


# Добавьте возможность сохранять и восстанавливать данные из файла (бинарная запись).

def openFile(fileName):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + fileName, "rb") as file:
        return pickle.load(file)
    
def writeToFile(fileName, data):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + fileName, "wb") as file:
        pickle.dump(data, file)

# Добавьте обработку исключений при чтении и записи файла.

def chooseOpenFile():
    answer = "y"
    while(True):
        print('Load data from file? y/n')
        ans = input()
        if ans == answer:
            print('type file name: ')
            fileName = input()
            try:
                data = openFile(fileName)
                return True, data
            except Exception as e:
                print(e)
                print('Try again? y/n')
                ans = input()
                if ans != answer:
                    return False, None
        else:
            return False, None


def chooseSaveDataToFile(data):
    answer = "y"
    while(True):
        print('Save data to file? y/n')
        ans = input()
        if ans == answer:
            print('type file name: ')
            fileName = input()
            try:
                writeToFile(fileName, data)
                print('success')
                return
            except Exception as e:
                print(e)
                print('Try again? y/n')
                ans = input()
                if ans != answer:
                    return 
        else:
            return 