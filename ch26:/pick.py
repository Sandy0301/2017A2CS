import pickle
class CarRecord:
    def __init__(self):
        self.VheicleID=''
        self.Registration=' '
        self.DeteOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00

Car=[0]*100
for i in range (100):
    Car[i]=CarRecord()
Car[2].EngineSize=2000
