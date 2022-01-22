from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""
    p = (52.2053, 0.1218)

    #Build list of stations
    stations = build_station_list()

    #find distances
    distances = stations_by_distance(stations, p)

    #isolate the first 10 stations, then change the format to the desired output format
    first = distances[:10]
    for i in range(len(first)): #iterate over each tuple in the list, changing the format as we go
        distance = first[i]
        first[i] = (distance[0].name, distance[0].town, distance[1])
    
    #print out
    print("10 closest stations:")
    print(first)

    #isolate the last 10, then change format and print
    last = distances[-10:]
    for i in range(len(last)):
        distance = last[i]
        last[i] = (distance[0].name, distance[0].town, distance[1])

    print("10 furthest stations:")
    print(last)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()