#27.06 Sandy
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
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist, end='')
        print(self.__ItemID, ' ; ', self.__OnLoan,';',self.__DueDate)
    
class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self, b):
        self.__IsRequested = True
        self.__RequestedBy = b

    def PrintDetails(self):
        print('')
        print("Book Details")
        LibraryItem.PrintDetails(self)
        if self.__IsRequested :
            print('Requested by  No.', self.__RequestedBy)
        else :
           print('no requests')

class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
    def PrintDetails(self):
        print('')
        print("CD details")
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

def main():
    ThisBook1=Book('12 Rules for Life', "Jordan Peterson", 7918)
    ThisBook1.SetIsRequested(101)
    ThisBook1.PrintDetails()
    ThisBook2 = Book("White Fang", "Jack London", 6234)
    ThisBook2.SetIsRequested(613)
    ThisBook2.PrintDetails()
    ThisBook3 = Book("Firefly Lane", "Whillih Hannah", 4917)
    ThisBook2.SetIsRequested(292)
    ThisBook2.PrintDetails()
    ThisCD1 = CD("And Jutice For All", "Metallica", 2901)
    ThisCD1.SetGenre('rock and roll')
    ThisCD1.PrintDetails()
    ThisCD2 = CD("Melody of The Night", "Pianoking", 2901)
    ThisCD2.SetGenre('Light Music')
    ThisCD2.PrintDetails()

main()
    
