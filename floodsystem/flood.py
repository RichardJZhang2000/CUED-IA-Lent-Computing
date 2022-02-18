from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """ This method takes a list of MonitoringStations objects
    stations and a float tol, and returns a list of tuples, where
    the first element within each tuple is a MonitoringStation object
    with relative water level larger than tol, and the second element
    in the tuple is its relative water level. The return list will be
    sorted in descending order of relative water level.
    """

    #creates a list of station-relative water level tuples, each element of which will only be created
    #if the relative water level is defined and exceeds the threshold
    levels = [(station, station.relative_water_level()) for station in stations
    if station.relative_water_level()!=None and station.relative_water_level()>tol]

    #sorts the tuples by descending order of water level
    levels = sorted_by_key(levels, 1, reverse=True)
    return levels

def stations_highest_rel_level(stations, N):
    """ This method takes a list of MonitoringStations objects stations
    and an integer N, and returns a list of the N stations (MonitoringStations
    objects) where the relative water level is highest. The returned list
    will be sorted by descending order of relative level.
    """

    #create a list of tuples where the relative water level is displayed after
    #the station, which allows usage of the sorted_by_key method
    levels = [(station, station.relative_water_level()) for station in stations]
    levels = sorted_by_key(levels, 1, reverse=True)
    stations_N = [levels[i][0] for i in range(N)]
    return stations_N