class CarRecord:
    def __init__(self):
        self.VehicleID = ''
        self.Registration = ' '
        self.DateOfRegistration = ''
        self.EngineSize = 0
        self.PurchasePrice = 0.00

ThisCar = CarRecord()
ThisCar.EngineSize = 2000

import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID=''
        self.Registration = ' '
        self.DateOfRegistration = ''
        self.EngineSize = 0
        self.PurchasePrice = 0.00
Car = [0]*100
for i in range(100):
    Car[i]=CarRecord()

Car[2].VehicleID='1234'
Car[2].EngineSize=2000
Car[2].Registration='X'
Car[2].DateOfRegistration='Feb 26, 2018'
Car[2].PurchasePrice='300000.00'


CarFile=open('Cars.DAT','wb')
for i in range (100):
    pickle.dump(Car[i],CarFile)
CarFile.close()

CarFile=open('Cars.DAT','rb')
Car=[]
for i in range(5):
    Car.append(pickle.load(CarFile))
for i in range(5):
    print (Car[i].VehicleID,Car[i].EngineSize,Car[i].DateOfRegistration,Car[i].PurchasePrice)

    CarFile.close()
