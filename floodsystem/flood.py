from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """ This method takes a list of MonitoringStations objects
    stations and a float tol, and returns a list of tuples, where
    the first element within each tuple is a MonitoringStation object
    with relative water level larger than tol, and the second element
    in the tuple is its relative water level. The return list will be
    sorted in descending order of relative water level.
    """

    levels = [(station, station.relative_water_level()) for station in stations if station.relative_water_level()!=None
    and station.relative_water_level>tol]

    levels = sorted_by_key(levels, 1, reverse=True)
    return levels