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
    rivers = {station.river for station in stations}
    return rivers