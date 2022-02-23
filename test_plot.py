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
    stations_N = stations_highest_rel_level(stations, 3)
    
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

def test_plot_water_level_with_fit():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Find the 10 stations with highest relative level
    stations_N = stations_highest_rel_level(stations, 3)

    #Plot the water level data of the past 2 days for the 5 stations with the highest levels,
    #with polynomial fit of degree 4
    dt=2
    count = 1
    for station in stations_N:
        dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
        if len(levels) > 0:
            plot_water_level_with_fit(station, dates, levels, 4)
            count -= 1
            if count == 0:
                break
