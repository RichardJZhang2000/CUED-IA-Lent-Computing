from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib as plt

def run():
    stations = build_station_list()
    update_water_levels(stations)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()