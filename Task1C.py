from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""
    p = (52.2053, 0.1218)

    #Build list of stations
    stations_list = build_station_list()

    #find stations within radius
    stations = stations_within_radius(stations_list, p, 10)

    #keep the names of the stations and delete all other information
    stations = [station.name for station in stations]

    #sort by name, then print
    stations = sorted(stations)
    print(stations)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()