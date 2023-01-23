class UndergroundSystem:
    def __init__(self):
        self.person = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.person[id]
        time_taken = t-startTime
        tup = (startStation, startTime)
        if tup not in self.times:
            self.times[tup] = [time_taken, 1]
        else:
            self.times[tup][0] += time_taken
            self.times[tup][1] += 1
        del self.person[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tup = (startStation, endStation)
        return self.times[tup][0] / self.times[tup][1]
