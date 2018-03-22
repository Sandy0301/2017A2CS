#pre release material
##task1
1.1
To set up a structure based on the structure of the data with elementary components and composite components for the program to handle.
1.2
star:repetition
circle:to choose one
1.3
While 
>CALL ReadSalary()
>>IF Salary>50:
>>>THEN
>>>>IF Salary>=90
>>>>>Then
>>>>>>Role-Project Manager
              
>>>>>Else
>>>>>>Role-Lead Developer
       
>>>ENDIF

>>ELSE
>>>Role-Manager

>ENDIF

ENDWHILE
1.4
see the image in the same folder
1.5
While 
>CALL ReadSalary()
>>IF Salary>50:
>>>THEN
>>>>IF Salary>90
>>>>>THEN
>>>>>>Role<-Project Manager
              
>>>>>Else
>>>>>>IF Salary>=70
>>>>>>>THEN 
>>>>>>>>Role<-Consultant

>>>>>>>ELSE
>>>>>>>>Role<-lead developer

>>>>>>ENDIF    

>>>>>ENDIF   

>>>ENDIF

>>ELSE
>>>Role-Manager

>ENDIF

ENDWHILE

1.6
def Role(s):
>if s<50:
>>return (“manager”)

>if s>=90:>>return (“Project Manager”)    
>if s<70:>>return (“Consultant”)    
>else:>>return (“Lead Developer”)

##task2
2.1
toy-Name,ID,Price, Minimum age
ComputerGame-category,console
Vehicle-type,height,length,weight
2.2
attributes of the base class are copied to the subclasses
see the diagram attached in the same folder
2.3
class Toy:>def __init__(self, Name, ID,  Price, Minimumage):>>self.__Name= Nameself.__ID= IDself.__Price= Priceself.__Minimumage= Minimumage>def Constructor(self):>>self.Name=""self.ID=0self.Price=-1self.__Minimumage=-1    
>def SetName(self,N):>>self.Name=N>def SetID(self,N):>>self.ID=N    
>def SetPrice(self,P):>>self.Price=P    
>def SetMinimuage(self,N):>>self.MinimumTOyage=Minimumage    
>def GetName(self):>>return(self.__Name)
    
>def GetID(self):>>return(self.__ID)   
>def GetPrice(self):>>return(self.__Price)    
>def GetMinimumage(self):>>return(self.__Minimumage)  
>def Output(self):>>print("Name:", self.GetName(),"ID:", self.GetID(),"Price:",self.GetPrice(),"MinimumAge:",self.GetMinimumage())
2.4,2.5
class ComputerGame(Toy):>def __init__(self, N, I, P, M, C, Con):>>Toy.__init__(self,N, I, P, M)self.__Category =Cself.__Console = Con>def Constructor(self):>>self.Constructor()self.Category = ""slef. Console ="">def SetCategory(self, C):>>self.Category = C>def SetConsole(self, Con):>>self.Console= Con>def GetCategory(self):>>return(self.__Category)>def GetConsole(self):>return(self.__Console)>def Output(self):>>print("Name:", self.GetName(),"ID:", self.GetID(),"Price:",self.GetPrice(),"MinimumAge:",self.GetMinimumage())print("Category:", self.GetCategory(), "Console:", self.GetConsole())        class Vehicle(Toy):>def __init__(self, N, I, P ,M ,T, H, L, W):>>Toy.__init__(self,N, I, P, M)self.__Type=Tself.__Height=Hself.__Length=Lself.__Weight= W>def Constructor(self):>>self.Constructor()>def SetHeight(self,H):>>self.Height=H>def SetLength(self,L):>>self.Length=L>def SetWeight(self,W):>>self.Weight=W>def GetHeight(self):>>return(self.__Height)>def GetLength(self):>>return(self.__Length)>def GetWeight(self):>>return(self.__Weight)>def Output(self):>>print("Name:", self.GetName(),"ID:", self.GetID(),"Price:",self.GetPrice(),"MinimumAge:",self.GetMinimumage())print("Weight:", self.GetWeight(), "Height:", self.GetHeight(), "length:", self.GetLength(), "Weight:", self.GetWeight())
2.6
a=Vehicle("red Sports Car", "RSC13", 15.00,6,"car",3.3,12.1,0.08)b=ComputerGame(“Garden”,”RSC20”, 250.00,”Construction”, “Camstation”)c=Toy(“Dancing bear”, “RSC03”,489.00,0,18)list=[a,b,c]
2.7
def find(name):
>for i in range(len(list)):
>>if list[i].GetID()==name:
>>>list[i].Output()
2.8
def discount(d):
>d=input(‘enter discount rate’)
for i in range (100):
>>Price=Price-0.01*d
return Price
2.9
Bubble sort:repeat steps through the sorted list by comparing adjacent items and switch their order if the program returns true

Insertion sort: sorting the data from the top, and hold the last one as current data
2.10
def arrange():>for j in range(len(list)):>>for i in range(len(list)-1):>>>if list[i].GetPrice()>list[i+1].GetPrice():>>>>temp= list[i]list[i]=list[i+1]list[i+1]=temp>return(list)

