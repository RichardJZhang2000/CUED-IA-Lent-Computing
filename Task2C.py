from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Find the 10 stations with highest relative level
    stations_N = stations_highest_rel_level(stations, 10)

    # Print out the stations' names and relative water levels
    for i in range(10):
        print(stations_N[i].name, stations_N[i].relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()