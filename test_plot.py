"""Unit test for plot module"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import *

def test_plot_water_levels():
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Find the 10 stations with highest relative level
    stations_N = stations_highest_rel_level(stations, 8)
    
    dt=10
    count = 1
    for station in stations_N:
        dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
        if len(levels) > 0:
            plot_water_levels(station, dates, levels)
            count -= 1
            if count == 0:
                break