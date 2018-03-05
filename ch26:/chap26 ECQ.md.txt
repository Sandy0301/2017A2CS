#This is the answer for end of chapter 26 questions.
##Sandy Op3

#### python
1.a i
class CustomerRecord:
	def __init__(self) :     	self.CustomerID = 0     	self.CustomerName = ''     	self.TelNumber = ''     	self.TotalOrders = 0
ii
CustomerData=[CustomerRecord() for i in range(1000)]
b.i
def Hash(CustomerID):
	Address=CustomerID%100
	return (Address)
ii
def AddRecord(CustomerData,Customer)
	Address=Hash(Customer.CustomerID)
	while CustomerData(Address).CustomerID!=0:
		Address=Address+1
	CustomerData[Address]=Customer
iii
def FindRecord(CustomerData,CustomerID)
	Address=Hash(CustomerID)
	while CustomerData[Address].CustomerID!=0:
		Address=Address+1
	return (Address)
c
import pickle
def Store(CustomerData):
	file=open(‘CustomerData.DAT’,’wb’)
	for i in range(1000):
	pickle.dump(CustomerData[i],file)
	file.close()
d
fixed lengths of records are required. It is also not necessary to write the save function, but adding and finding are needed.

####2
def OpenFile():
	name=input(‘which file do you want to use?’)
	try:
		read=open(name,’rb+’)
	except:
		break