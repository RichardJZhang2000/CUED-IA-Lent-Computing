# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module"""

from floodsystem.analysis import *
from floodsystem.stationdata import build_station_list, update_water_levels

def test_polyfit():
    poly, d0 = polyfit([1,2,3],[1,2,3],3)

def test_normalize():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        assert station.relative_water_level()==normalize(station.latest_level, station)