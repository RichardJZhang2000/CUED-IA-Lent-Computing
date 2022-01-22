"""Unit test for geo module"""

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

    
    
