##task2
2.1
see the image in the same folder
2.2
attributes of the base class are copied to the subclasses
see the diagram attached in the same folder
2.3
class Toy:
>def SetName(self,N):
>def SetPrice(self,P):
>def SetMinimuage(self,N):
>def GetName(self):
    
>def GetID(self):
>def GetPrice(self):
>def GetMinimumage(self):
>def Output(self):
2.4
class ComputerGame(Toy):
2.5
class Toy:
>def SetMinimumAge(self, M):
>>if M>18 or M<0:
>>>print('not valid')
		
>>else:
>>>self.__MinimumAge=M
2.6
a=Vehicle("red Sports Car", "RSC13", 15.00,6,"car",3.3,12.1,0.08)
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
def arrange(list):