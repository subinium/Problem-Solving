class UndergroundSystem:
    
    def __init__(self):
        self.id = dict()
        self.travel = defaultdict(int)
        self.travel_cnt = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sp, tp = self.id[id]
        self.travel[(sp, stationName)] += t-tp
        self.travel_cnt[(sp, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travel[(startStation, endStation)]/self.travel_cnt[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)