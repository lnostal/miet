from enum import Enum

class Book:

    def __init__(self,title,author,publisher,pages,cost):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__pages = pages
        self.__cost = cost

    def costOfPage(self):
        return self.getCost() / self.__pages
    
    def getCost(self):
        if str(self.__title).lower().__contains__("программировани"):
            return self.__cost * 2

        return self.__cost
    
    def __str__(self):
        return "<{3}>:\n\ttitle: \t\t{0}\n\tauthor: \t{4}\n\tpublisher: \t{5}\n\tpages: \t\t{1}\n\tcost: \t\t{2}".format(self.__title, self.__pages, self.__cost, type(self), self.__author, self.__publisher)
    
    def __bytes__(self):
        return r''


class AudioBook(Book):
    def __init__(self,title,author,publisher,pages,cost,read):
        Book.__init__(self,title,author,publisher,pages,cost)
        self.__read = read

    def __str__(self):
        return super().__str__() + "\n\tread: \t\t{}".format(self.__read)

class ForeignBook(Book):
    def __init__(self,title,author,publisher,pages,cost,interpreter):
        Book.__init__(self,title,author,publisher,pages,cost)
        self.__interpreter = interpreter

    def __str__(self):
        return super().__str__() + "\n\tinterpreter: \t{}".format(self.__interpreter)

class ForeignAudioBook(AudioBook,ForeignBook):
    def __init__(self,title,author,publisher,pages,cost,read,interpreter):
        ForeignBook.__init__(self,title,author,publisher,pages,cost,interpreter)
        AudioBook.__init__(self,title,author,publisher,pages,cost,read)
        

class BookType(Enum):
    Classic = 1         # base
    Audio = 2 
    ForeignClassic = 3
    ForeignAudio = 4

