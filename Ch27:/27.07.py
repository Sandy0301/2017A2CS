#27.07 Sandy
import datetime
class Borrower():
    def __init__(self,bn,ea,bi):
        self.__BorrowerName=bn
        self.__EmailAddress=ea
        self.__BorrowerID=bi
        self.__ItemsOnLoan=0
    def getBorrowerName(self):
        return (self.__BorrowerName)
    def getEmailAddress(self):
        return (self.__EmailAddress)
    def getBorrowerID(self):
        return (self.__BorrowerID)
    def getItemsOnLoan(self):
        return (self.__ItemsOnLoan)
    def updateItemsOnLoan(self,bn):
        self.__ItemsOnLoan=self.__ItemsOnLoan+bn
    def printDetails(self):
        print(self.__BorrowerName,';',self.__BorrowerID,';',self.__EmailAddress,';',self.__ItemsOnLoan)


class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.BorrowerID=0
        self.__DueDate = datetime.date.today()
    def getTitle(self):
        return(self.__Title)
    def getAuthor_Artist(self):
        return (self.__Author_Artist)
    def getItemID(self):
        return(self.__ItemID)
    def getOnLoan(self):
        return(self.__OnLoan)
    def getBorrowerID(self):
        return (self.__BorrowerID)
    def getDueDate(self):
        return (self.__DueDate)
    def Borrowing(self,i,bk):
        if bk.GetItemsOnLoan()<=7:
            self.__OnLoan=True
            self.__BorrowerID = bk.getBorrowerID()
            self.__DueDate = self.__DueDate + datetime.timedelta(weeks=2)
            bk.updateItemsOnLoan(1)
        else:
            print('Unable. You can only borrow 7 books in total.')   
    def Return(self,i,bk):
        self.__OnLoan = False
        bk.UpdateItemsOnLoan(-1)
    def printDetails(self):
        print(self.__Title,';',self.__Author_Artist,';',self.__ItemID,';',self.__OnLoan,';',self.BorrowerID,';',self.__DueDate)


class Boook(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy=0
    def getIsRequested(self):
        return(self.__IsRequested)
    def getRequestedBy(self):
        return (self.__RequestedBy)
    def RequestBook(self,i,bk):
        self.__IsRequested = True
        self.RequestedBy=bk.getBorrowerID()
    def printDetails(self):
        LibraryItem.printDetails(self)
        print(self.__IsRequested,';',self.__RequestedBy)


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ''
    def getGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
    def printDetails(self):
        LibraryItem.printDetails(self)
        print(self.__Genre)

def menu():
    print('<1> add a borrower')
    print('<2> add a book')
    print('<3> add a CD')
    print('<4> borrow a book')
    print('<5> return a book')
    print('<6> borrow a CD')
    print('<7> return a CD')
    print('<8> request a book')
    print('<9> display details')
    print('<99>Exit')
    choice=int(input('Type in the figure of your request:' ))
    return (choice)

def main():
    end=False
    nbi=1
    nki=1
    nci=1
    while end==False:
        choice=menu()
        if choice==1:
            Name = input("Name         : ")
            Email = input("Email address: ");
            bi=nbi
            nbi=nbi+1
            B=Borrower(Name, Email, bi)
        elif choice == 2: 
            Title = input('Title  :')
            Author = input('Author:')
            i = nbi
            nbi = nbi + 1
            Bo = Book(Title, Author, i)
        elif choice == 3:
            Title = input("Title  : ")
            Artist = input("Artist: ")
            i = nci
            nci=nci+ 1
            C = CD(Title, Artist,i)
        elif choice == 4:   
            bi = input("Borrower ID: ")
            i = input("Book ID    : ")
            Bo.Borrowing(i, Borrower)
        elif choice == 5:   
            bi = input("Borrower ID: ")
            i= input("Book ID: ")
            Bo.Return(i, Borrower)
        elif choice == 6:    
            bi = input("Borrower ID: ")
            i= input("CD ID: ")
            CDCD.Borrowing(i, Borrower)
        elif choice == 7:     
            bi = input("Borrower ID: ")
            i = input("CD ID: ")
            CD.Return(i, Borrower)
        elif choice == 8:    
            bi = input("Borrower ID: ")
            i= input("Book ID: ")
            Bo.RequestBook(i, Borrower)
        elif choice == 9:   
            print("Borrower Details")
            Bo.printDetails()
            print("Book Details")
            Bo.printDetails()
            print("CD Details")
            CD.printDetails()
        elif choice == 99:
            end = True
        else:
            choice=main()
main()
