from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.checkin_map = {}
        self.journey_map = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, start_time = self.checkin_map[id]
        key = start_name + "-" + stationName
        self.journey_map[key].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "-" + endStation
        count = len(self.journey_map[key])
        total = sum(self.journey_map[key])
        return total / count
