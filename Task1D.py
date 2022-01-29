from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""

    #build list of stations
    stations_list = build_station_list()
    rivers = rivers_with_station(stations_list)
    
    #get the number of rivers in total
    number_of_rivers = len(rivers)

    #print the number of rivers and the first 10 rivers in alphabetical order
    print("{} stations. First 10 - {}".format(number_of_rivers, sorted(rivers)[:10]))

    #get the rivers and the stations on them
    stations_on_river = stations_by_river(stations_list)

    #print the name of the stations on the selected rivers
    for river in ["River Aire", "River Cam", "River Thames"]:
        station_names = [station.name for station in stations_on_river[river]]
        print("{} has the following stations: {}".format(river, sorted(station_names)))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()