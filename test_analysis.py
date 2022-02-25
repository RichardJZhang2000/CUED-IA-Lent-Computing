# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module"""

from floodsystem.analysis import *
from floodsystem.stationdata import build_station_list, update_water_levels

def test_polyfit():
    #just check it can run
    poly, d0 = polyfit([1,2,3],[1,2,3],3)

def test_normalize():
    #build station list and update water levels into them
    stations = build_station_list()
    update_water_levels(stations)

    #make sure that for stations with water levels, the normalize method gets the same result as the relative water level
    for station in stations:
        assert station.relative_water_level()==None or station.relative_water_level()==normalize(station.latest_level, station)

def test_rate():
    #build station list and write water levels into them
    stations = build_station_list()
    update_water_levels(stations)

    #get the ratings
    risks = rate(stations)

    for station in stations:
        assert station in risks.keys
        assert risks[station]=='severe' or risks[station]=='high' or risks[station]=='moderate' or risks[station]=='low'