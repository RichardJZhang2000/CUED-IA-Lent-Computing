from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""
    #Build list of all stations
    stations_list = build_station_list()

    #find stations with inconsistent data
    stations = inconsistent_typical_range_stations(stations_list)

    #keep the names of the stations and delete all other information
    stations = [station.name for station in stations]

    #sort by name, then print
    stations = sorted(stations)
    print(stations)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()