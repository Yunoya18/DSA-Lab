"""Labs 12.03"""
import json
def find_station():
    """find station"""
    city = set(json.loads(input()))
    num = int(input())
    station = []
    have = []
    for _ in range(num):
        info = json.loads(input())
        station.append((info["Name"], set(info["Cities"])))
    while True:
        if (not station) or (not station):
            break
        station.sort(key=lambda x: len(city.intersection(x[1])), reverse=True)
        if city.intersection(station[0][1]):
            city = city.difference(station[0][1])
            have.append(station[0][0])
        station.pop(0)
    have.sort()
    print(have)

find_station()
