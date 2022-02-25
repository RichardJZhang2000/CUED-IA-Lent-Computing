import datetime
import numpy as np
import matplotlib as plt

from floodsystem.datafetcher import fetch_measure_levels

def polyfit(dates, levels, p):
    '''A function that takes in a dates list, a level list, an int p, and returns the polynomial object that
    fits the data in degree p'''


    #Convert dates into float
    dates_float = plt.dates.date2num(dates)

    # Using shifted dates_float values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(dates_float - dates_float[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly, dates_float[0]


def rate(stations):
    """This function takes stations, a list of MonitoringStation objects,
    and outputs a dict, where the key is the station and the value is the
    flood risk assessment (severe, high, moderate, or low). this method 
    assumes the water levels have already been updated.

    The judging criteria used is a mixed weight of current relative water
    level, current rate of change of water level, current "acceleration" of water level,
    and predicted water level using a polynomial of degree 4. The rate of change and
    acceleration is computed using discrete values rather than extracted from the polyfit
    because of the possibility of overfitting.

    The calculated value for velocity and acceleration are compared to the last measurement,
    so it is natural to add them together to predict a "discrete" predicted velocity. Again,
    this is to guard against overfitting, but the added value should be close to the difference
    between the predicted and the current.

    Consider the following possibilities:
    Current water level 1.0, predicted 1.4, velocity 0.3, acceleration 0.1 --> severe
    Current water level 0.6, predicted 1, velocity 0.3, acceleration 0.1 --> high
    Current water level 0.9, predicted 1.0, velocity 0.1, acceleration 0 --> high
    Current water level 0.6, predicted 1.4, velocity 0.7, acceleration 0.1 --> severe
    Current water level 0.6, predicted 1.4, velocity 0.3, acceleration 0.1 (a case where the polyfit takes off) --> high
    
    Assuming the cutoffs are going to be 1, 0.8 and 0.5 between the four levels (similar to the
    rule of thumb for strong, moderate, and weak linear correlation), the above examples give a
    good indication for the boundary conditions of the metric.

    The above thought experiments indicate that a larger weight should be placed on current over predicted.

    A formula satisfying these requirements is:
    R = 0.5*C + 0.3*P + 0.5*(V + A)

    Where C is current, P is predicted, V is discrete velocity, and A is acceleration
    """
    risk = {}
    for station in stations:
        #skip the stations with no latest level or with an inconsistent typical range
        if station.latest_level==None or not station.typical_range_consistent():
            continue

        #find the predicted level and convert to relative level
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        if len(dates)==0: #for some reason this is a bug which sometimes appears; my instinct is that it has to do
            #with previous times with no data
            continue
        poly, _ = polyfit(dates, levels, 4)
        pred = poly(1) #predicted water level the next day
        pred_rel = normalize(pred, station)

        #extract other information necessary
        current = station.relative_water_level()
        velocity = normalize(levels[0], station) - normalize(levels[int(len(levels)/2)], station) #velocity over the last day
        acc = (normalize(levels[0], station) - normalize(levels[int(len(levels)/2)], station)
            ) - (normalize(levels[int(len(levels)/2)], station) - normalize(levels[-1], station))
        #acceleration given by change in velocity over the last two days
        #velocity and acceleration are taken over the range of one day so noises are negligible
        
        #calculate the metric
        metric = 0.5*current + 0.3*pred_rel + 0.5*(velocity+acc)

        #determine the risk and add to the dict
        if metric >1:
            risk[station] = 'severe'
        elif metric>0.8:
            risk[station] = 'high'
        elif metric>0.5:
            risk[station] = 'moderate'
        else:
            risk[station] = 'low'

    return risk

def normalize(num, station):
    #Just an internal helper method, should not be used externally
    return (num-station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
