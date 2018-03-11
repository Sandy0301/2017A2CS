#27.03 Sandy
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
        print('The borrower is',self.__BorrowerName)
        print('Borrower ID is',self.__BorrowerID)
        print('The email address is',self.__EmailAddress)
        print('The items on loan is',self.__ItemsOnLoan)

def main():
    b=Borrower('Jason','hello@rdfz.cn',1304)
    b.UpdateItemsOnLoan(3)
    b.PrintDetails()
main()
