# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from distutils.command.build import build
from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    #Create three stations, the first of which has consistent data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    
    #Create a monitoring station from the data and test its consistency
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.typical_range_consistent()==True


    #-----------------------------------------
    #The second station has unavailable data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    
    #Create a monitoring station from the data and test its consistency
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.typical_range_consistent()==False


    #------------------------------------------
    #The third station has inconsistent data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (3.4, -2.3)
    river = "River X"
    town = "My Town"
    
    #Create a monitoring station from the data and test its consistency
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.typical_range_consistent()==False

def test_inconsistent_typical_range_stations():
    #Create three stations as before and compile them into a list
    s1 = MonitoringStation("test-s-id", "test-m-id", "some station", (-2.0, 4.0), (-2.3, 3.4445), "River X", "My Town")
    s2 = MonitoringStation("test-s-id", "test-m-id", "some station", (-2.0, 4.0), None, "River X", "My Town")
    s3 = MonitoringStation("test-s-id", "test-m-id", "some station", (-2.0, 4.0), (3.4, -2.3), "River X", "My Town")
    s = [s1, s2, s3]

    assert inconsistent_typical_range_stations(s)==[s2, s3]

def test_relative_water_level():
    #Build station list
    stations = build_station_list()

    #add the water levels into the 5 stations
    update_water_levels(stations)

    #generate a list of relative water levels
    rel = [station.relative_water_level() for station in stations]

    #make sure there are as many relative water levels as there are stations
    assert len(rel)==len(stations)

    for i in range(len(rel)):
        #check relative water levels against manual calculations
        assert rel[i] == None or rel[i]==(stations[i].latest_level-stations[i].typical_range[0])/(stations[i].typical_range[1]-stations[i].typical_range[0])
