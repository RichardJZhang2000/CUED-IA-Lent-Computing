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
