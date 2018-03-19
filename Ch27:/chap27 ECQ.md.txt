# Chapter 27 ECQ  Sandy S3C3
## 1.
a
```mermaid
graph LR
A[PersonalAccount]-->B[BankAccount]
C[SavingAccount]-->B
```
b
class BankAccount :
>def \_\_init\_\_(self, i): 
>>self.__AccountHolderName = ''
>>self.__IBAN = i 

>def SetAccountHolderName(self, n):
>>self.__AccountHolderName = n 

>def GetAccountHolderName(self):
>>return(self.__AccountHolderName) 
	
>def GetIBAN(self):
 >>return(self.__IBAN)
 
 c. i
Attribute: MonthlyFee, OverDraftLimit 
Method: Constructor, SetOverDraftLimit, GetOverDraftLimit, GetMonthlyFee

ii. attribute: InterestRate  
method: Constructor, GetInterestRate, CalculateInterest

iii. Encapsulation

## 2
a. 
```mermaid
graph LR
A[Pay-As-You-Go-TicketHolder]-->B[SeasonTicketHolder]
C[ContractHolder]-->B
```
EmailAddress : STRING
GetTicketHolderName()
GetEmailAddress()
                                                      
PRIVATE                          
Amount : CURRENCY        
PUBLIC
Constructor(Name: STRING, email : STRING)
GetAmount() 
UpdateAmount()

PRIVATE
MonthlyFee : CURRENCY
PUBLIC
Constructor(Name: STRING, email : STRING, Fee : CURRENCY)
GetFee()

b. i
Because they will be allowed to change in the' class ' function
ii To get access to the attribute
c
NewCustomer = ContractTicketHolder("A. Smith", "xyz@abc.xx", 10)
## 3
a
Node is to direct the order in the Queue class
b
class NodeClass : 
>def \_\_init\_\_(self):
>>self.__d = ''
self.__p=-1 

 >def SetData(self, d):
      >>self.__d= d 

> def GetData(self):
      >>return(self.__d) 

 >def SetPointer(self, x):
      >>self.__d = x 

 >def GetPointer(self):
      >>return(self.__p)

c
class QueueClass:
>def\_\_init\_\_(self):
>>self.__Queue = \[NodeClass() for i in range(51)\]
      self.__Head = -1
      self.__Tail = -1 

d
>def JoinQueue(self, d):
      >>if Head == -1 : 
>>> Head = 0
    
>>self.__Tail += 1  
      i = self.__Tail 
 self.__Queue\[i\].SetData(d)