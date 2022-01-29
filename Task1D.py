from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""

    #Build list of stations
    stations_list = build_station_list()
    rivers = rivers_with_station(stations_list)
    number_of_rivers = len(rivers)
    print("{} stations. First 10 - {}".format(number_of_rivers, sorted(rivers)[:10]))

    stations_on_river = stations_by_river(stations_list)
    for river in ["River Aire", "River Cam", "River Thames"]:
        station_names = [station.name for station in stations_on_river[river]]
        print("{} has the following stations: {}".format(river, sorted(station_names)))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()