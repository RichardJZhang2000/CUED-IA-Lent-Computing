# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """This method checks that the data for the typical
        high/low ranges for the station is available and 
        consistent (i.e. high>low).
        Return is True if the data is BOTH available AND 
        consistent, and False is either criterion is not met.
        """
        #if the typical range is unavailable, return False
        if self.typical_range==None:
            return False
        
        #if the first item in typical range (the low) is higher
        #than the second (the high), return False
        if self.typical_range[0] > self.typical_range[1]:
            return False
        
        #if neither of the above are True, then the data is consistent
        #so return True
        return True

    def relative_water_level(self):
        """ This method returns the latest water level as a fraction
        of the typical range. If the typical range is inconsistent or
        unavailable, the method returns None. Otherwise, a typical low
        would correspond to a value of 0.0 and a typical high would 
        correspond to a value of 1.0.
        """
        #If the typical range is inconsistent or unavailable or the latest level is not available, return None
        if not self.typical_range_consistent() or self.latest_level==None:
            return None

        #Calculate relative water level
        rel = (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
        return rel

def inconsistent_typical_range_stations(stations):
    """This function takes stations, a list of MonitoringStation
    objects, and outputs a list of MonitoringStation objects which
    are in stations but have an inconsistent typical range
    """

    incon_stations = [station for station in stations if not station.typical_range_consistent()]
    return incon_stations
