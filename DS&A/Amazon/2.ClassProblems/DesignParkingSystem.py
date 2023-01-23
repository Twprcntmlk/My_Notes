class ParkingSystem:
    def __init__(self):
        self.ParkingSlots = [None]*1000
        self.SizeChart= {"small":0 ,"medium":10, "large":25}
        self.RateChart= {0:(1,15),1:(2,24),2:(4,40),3:(8,75),4:(12,100)}

    def checkIn(self, size: str, time: int) -> None:
        for idx, slot in enumerate(self.ParkingSlots):
            if slot == None:
                self.ParkingSlots[idx]=[size, time]
                break
            elif idx == len(self.ParkingSlots)-1:
                return "Parking Lot Full"


    def checkOut(self, id: int, time: float) -> None:
        carSize = self.ParkingSlots[id][0]
        enterTime = self.ParkingSlots[id][1]
        #############################################
        self.ParkingSlots[id] = None
        return self.getCost(enterTime,time,carSize)


    def getCost(self, startTime: float, endTime: float, size: str) -> float:
        timeInGarage=endTime-startTime
        print("timeInGarage",timeInGarage)
        rateCost=0
        sizeCost=self.SizeChart[size]
        #########################################
        for idx in range(len(self.RateChart)-1):
            rateHour, ratePrice = self.RateChart[idx+1]
            prevRateHour, prevRatePrice = self.RateChart[idx]

            if timeInGarage < 1:
                rateHour, ratePrice = self.RateChart[0]
                rateCost=ratePrice
                break
            elif  prevRateHour <= timeInGarage < rateHour :
                rateCost=prevRatePrice
                break
            else:
                rateHour, ratePrice = self.RateChart[4]
                rateCost=ratePrice

        return rateCost+sizeCost

garage1= ParkingSystem();

print(garage1.checkIn("medium",2))
print(garage1.checkIn("large",4))
print(garage1.checkOut(0,12))
print(garage1.checkOut(1,12))
print(garage1.checkIn("medium",6))
print(garage1.checkIn("large",7))
print(garage1.checkIn("large",10))
print(garage1.checkIn("medium",12))
print(garage1.checkOut(0,6.5))
print(garage1.checkOut(1,8))
print(garage1.checkOut(2,13))
print(garage1.checkOut(3,20))
