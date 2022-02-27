from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import rate
import matplotlib as plt

def run():
    #build the station list and update the water levels
    stations = build_station_list()
    update_water_levels(stations)

    #rate the risks of the stations
    risk = rate(stations)
    #convert them to lists based on the level of risk and print those lists
    severe = [station.name for station in risk.keys() if risk[station]=='severe']
    high = [station.name for station in risk.keys() if risk[station]=='high']
    mod = [station.name for station in risk.keys() if risk[station]=='moderate']
    low = [station.name for station in risk.keys() if risk[station]=='low']

    print('Severe:', severe)
    print('High:', high)
    print('Moderate:', mod)
    print('Low:', low)
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()