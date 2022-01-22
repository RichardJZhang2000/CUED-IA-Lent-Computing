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
    type) and a coordinate p (tuple of floats) and calculates the
    distance (haversine) of each station to the coordinate defined
    by p.
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