import pickle
CarFile=open('Cars.DAT','rb')
Car=[]
for i in range(100):
    Car.append(pickle.load(CarFile))
for i in range(100):
    print(Car[i].VehicleID,Car[i].EngineSize,Car[i].DataOfRegistration,Car[i].Registration,Car[i].PurchasePrice)
CarFile.close()
