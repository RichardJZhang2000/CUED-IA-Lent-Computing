import numpy as np
import matplotlib as plt

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
    flood risk assessment (severe, high, moderate, or low).

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
