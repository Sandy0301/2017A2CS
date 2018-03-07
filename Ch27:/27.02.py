import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
    def GetTitle(self):
        return(self.__Title)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist, end='')
        print(self.__ItemID, ' ; ', self.__OnLoan,';',self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy=0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self):
        self.__IsRequested = True

class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
def main():
    ThisBook = Book("12 Rules for Life", "Jordan Peterson", 7918)
    ThisCD = CD("And Jutice For All", "Metallica", 2901)
    ThisBook.PrintDetails()
    ThisCD.PrintDetails()
    ThisBook2 = Book("White Fang", "Jack London", 6234)
    ThisCD2 = CD("Dark Side Of The Moon", "Pink Floyd", 1023)
    ThisBook2.PrintDetails()
    ThisCD2.PrintDetails()
    ThisBook3 = Book("Firefly Lane", "Whillih Hannah", 7918)
    ThisCD3 = CD("Melody of The Night", "Pianoking", 2901)
    ThisBook3.PrintDetails()
    ThisCD3.PrintDetails()
main()

