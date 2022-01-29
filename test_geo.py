"""Unit test for geo module"""

from sympy import Dict
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    station_list = build_station_list()
    test_stations = station_list[0:3]
    p = (53, -1) #somewhere close to some stations
    distances = stations_by_distance(test_stations, p)

    #make sure that there are 3 tuples in the result
    assert len(distances)==3

    #make sure the list is sorted in order of the distance
    assert distances[0][1]<=distances[1][1]
    assert distances[1][1]<=distances[2][1]

    for i in range(3):
        station = distances[i][0]
        #make sure the stations are within the list of test stations
        assert distances[i][0].station_id==test_stations[0].station_id or distances[i][0].station_id==test_stations[1].station_id or distances[i][0].station_id==test_stations[2].station_id

        #make sure the distances are calculated correctly
        assert haversine(station.coord, p)==distances[i][1]

def test_stations_within_radius():
    #get the list of stations and define a centre
    station_list = build_station_list()
    p = (53, -1)

    #get the list of stations within 10km
    stations = stations_within_radius(station_list, p, 10)

    for station in station_list:
        if haversine(station.coord, p)<=10:
            #for each station in the entire list, if it lies within 10km of the centre,
            #then it should appear once in the stations list; else, it should not appear
            assert stations.count(station)==1
        else:
            assert stations.count(station)==0

def test_rivers_with_station():
    #get the list of stations and create the set of rivers
    station_list = build_station_list()
    rivers = rivers_with_station(station_list)

    #test if rivers is a set object
    assert type(rivers) is set

def test_stations_by_river():
    #get the list of stations and create the river-station dictionary
    stations_list = build_station_list()
    river_station_dict = stations_by_river(stations_list)

    #test if river_station_dict is a dictionary object
    assert type(river_station_dict) is dict

    #test if an value in river_station_dict is a list
    assert type(river_station_dict["River Cam"]) is list

def test_rivers_by_station_number():
    #get the list of stations and create the rivers_ranking list
    stations_list = build_station_list()
    rivers_ranking = rivers_by_station_number(stations_list, 9)

    #check if rivers_ranking is a list
    assert type(rivers_ranking) is list

    #check if the elements in rivers_ranking are tuples
    assert type(rivers_ranking[0]) is tuple