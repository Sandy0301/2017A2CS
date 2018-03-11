#27.05 Sandy
import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID=0
    def GetTitle(self):
        return(self.__Title)
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist, end='')
        print(self.__ItemID, ' ; ', self.__OnLoan,';',self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = 'Not requested'
        self.__RequestedBy=0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def PrintDetails(self):
        print("Book details:")
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested)

class Borrower():
    def __init__(self,bn,ea,bi):
        self.__BorrowerName=bn
        self.__EmailAddress=ea
        self.__BorrowerID=bi
        self.__ItemsOnLoan=0
        
    def GetBorrowerName(self):
        return (self.__BorrowerName)
    def GetEmailAddress(self):
        return (self.__EmailAddress)
    def GetBorrowerID(self):
        return (self.__BorrowerID)
    def GetItemsOnLoan(self):
        return (self.__ItemsOnLoan)
    def UpdateItemsOnLoan(self,i):
        self.__ItemsOnLoan=self.__ItemsOnLoan+i
    def PrintDetails(self):
        print('')
        print('The borrower is',self.__BorrowerName)
        print('Borrower ID is',self.__BorrowerID)
        print('The email address is',self.__EmailAddress)
        print('The items on loan is',self.__ItemsOnLoan)


def main():
    ThisBook = Book("12 Rules for Life", "Jordan Peterson", 7918)
    b=Borrower('Jason','hello@rdfz.cn',103)
    b.PrintDetails()
    b.UpdateItemsOnLoan(3)
    ThisBook.PrintDetails()
    ThisBook2 = Book("The warriors", 'James Dashner', 3790)
    b=Borrower('Amy','Amyyy@163.com',129)
    b.PrintDetails()
    b.UpdateItemsOnLoan(0)
    ThisBook.PrintDetails()

main()

    
