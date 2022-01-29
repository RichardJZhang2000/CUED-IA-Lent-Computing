from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""

    #Build list of stations
    stations_list = build_station_list()

    #print the top 9 rivers with the most number of stations, but including rivers that are tied in numbers
    print(rivers_by_station_number(stations_list, 9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()