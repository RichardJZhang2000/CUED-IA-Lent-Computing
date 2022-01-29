# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """ This function takes a list of stations (MonitoringStation
    type) and a coordinate p (tuple of 2 floats, latitude then longitude)
    and calculates the distance (haversine) of each station to the
    coordinate defined by p.
    The return is a list of tuples, each of which contains a
    station (MonitoringStation type) and the corresponding distance (float)
    """

    distances = []
    for station in stations:
        coord = station.coord
        dist = haversine(coord, p)
        distances.append((station, dist))
    
    distances = sorted_by_key(distances, 1)
    return distances

def stations_within_radius(stations, centre, r):
    """ This function takes a list of stations (MonitoringStation
    type), a centre (tuple of 2 floats, latitude then longitude)
    and a distance r, and returns a list of all the stations
    (MonitoringStation type) which lie within a distance r of the
    centre.
    The distance r should be in units of kilometre (km).
    """
    #find distances from each station to the centre (in km), and then sort by distance
    distances = [(station, haversine(station.coord, centre)) for station in stations]
    distances = sorted_by_key(distances, 1)

    #find the location of the first station which exceeds r from the centre
    i=0
    while distances[i][1]<r:
        i+=1
    
    #select all stations before the index i
    stations = [distances[j][0] for j in range(i)]
    return stations

def rivers_with_station(stations):
    """This function takes in a list of stations (MonitoringStation type),
    and returns a set of strings, containing the names of rivers that have a station."""

    #Create a set of rivers that have stations
    rivers = {station.river for station in stations}

    return rivers

def stations_by_river(stations):
    """This function takes in a list of stations (MonitoringStation type),
    and returns a dictionary with river names as keys and a list of stations on the 
    respective river as values"""
   
    #Create an empty dictionary to hold the river-station pairs
    river_station_dict = {}

    #Iterate over the list of station objects
    for station in stations:

        #If the river is already a key in the dictionary, append the station object in the value (a list)
        if station.river in river_station_dict.keys():
            river_station_dict[station.river].append(station)

        #If the river is not a key, create a new entry with the river as key and station as value
        else:
            river_station_dict[station.river] = [station]

    return river_station_dict

def rivers_by_station_number(stations, N):
    """This function takes in a list of stations (MonitoringStation type),
    and a number (int type), and returns a list of (river name, number of stations)
    tuples, sorted by the number of stations. In the case that there are more rivers 
    with the same number of stations as the N th entry, these rivers are included in the list."""

    #create empty list to hold the tuples and get stations list
    river_station_number = []
    stations_on_river = stations_by_river(stations)

    #convert the river-station string-object pair into list of tuples of river name and number of stations
    for pair in stations_on_river.items():
        river_station_number.append((pair[0], len(pair[1])))

    #sort the list of tuples by the number of stations
    river_station_number_sorted = sorted_by_key(river_station_number, 1, reverse=True)

    #cut the list of tuples according to N and return it
    counter = N
    while river_station_number_sorted[counter-1][1] == river_station_number_sorted[counter][1]:
        counter += 1
    return river_station_number_sorted[:counter]
