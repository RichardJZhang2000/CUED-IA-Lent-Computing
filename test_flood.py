from floodsystem.station import MonitoringStation
from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    #create the list of stations and update them with their water levels
    stations = build_station_list()
    update_water_levels(stations)

    stations_over = stations_level_over_threshold(stations, 0.5)

    #manually count the number of stations over the threshold
    count = 0
    for i in range(len(stations)):
        if stations[i].relative_water_level()!=None:
            if stations[i].relative_water_level()>0.5:
                count +=1

    #assert that the number of station-level tuples is the same as expected from the above count
    assert len(stations_over) == count

    for i in range(len(stations_over)):
        #make sure the first element in each tuple is a MonitoringStation object and the second is a float
        assert isinstance(stations_over[i][0], MonitoringStation)
        assert isinstance(stations_over[i][1], float)

        if i<len(stations_over)-1:
            #make sure the list is sorted in descending order of relative water level
            assert stations_over[i][1]>=stations_over[i+1][1]
            #make sure the list only contains items with relative water level larger than the threshold
            assert stations_over[i][1]>0.5

def test_stations_highest_rel_level():
    #build the list of stations and update water levels into them
    stations = build_station_list()
    update_water_levels(stations)

    #create the list of N stations
    stations_N = stations_highest_rel_level(stations, 20)

    #make sure it is exactly N stations
    assert len(stations_N)==20

    for i in range(20):
        #make sure each element is a MonitoringStation object
        assert isinstance(stations_N[i], MonitoringStation)

        if i<19:
            #make sure it is sorted by descending order of relative water level
            assert stations_N[i].relative_water_level()>stations_N[i+1].relative_water_level()