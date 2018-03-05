import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = "0"
        self.Registration = " "
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00
Car = [0]*100
for i in range(100):
    Car[i]=CarRecord()

Car[3].VehicleID = "8888"
Car[3].EngineSize = 2000
Car[3].Registration = "D1"
Car[3].PurchasePrice = 500000.0

CarFile=open('Cars.DAT','wb')
for i in range(100):
    pickle.dump(Car[i],CarFile)
CarFile.close()

CarFile = open ('Cars.DAT','rb')
Car= []
for i in range(10):
    Car.append(pickle.load(CarFile))
for i in range(10):
    print(Car[i].VehicleID,Car[i].EngineSize,Car[i].DateOfRegistration,Car[i].Registration,Car[i].PurchasePrice)

CarFile. close ()
