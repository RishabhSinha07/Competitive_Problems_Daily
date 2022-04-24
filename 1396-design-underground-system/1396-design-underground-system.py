class UndergroundSystem:

    def __init__(self):
        self.user = {}
        self.stat = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = self.user[id][0]+'->'+stationName
        tlt = t - self.user[id][1]
        self.stat[key].append(tlt)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation+'->'+endStation
        return sum(self.stat[key])/len(self.stat[key])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)