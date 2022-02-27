import matplotlib.pyplot as plt
import matplotlib
from .analysis import polyfit

def plot_water_levels(station, dates, levels):
    '''This function takes in a MonitoringStation object, 
    a dates list and a levels list, and plots a graph of past
    water levels against dates.'''


    # Plot
    plt.plot(dates, levels, label="water level")
    plt.axhline(y=station.typical_range[0], color='b', linestyle='-', label="typical low")
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-', label="typical high")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''This function takes in a MonitoringStation object, 
    a dates list, a levels list and a degree p, and plots a graph of past
    water levels against dates, with a polynomial fit of degree p.'''

    #Convert dates object into float
    dates_float = matplotlib.dates.date2num(dates)

    #obtain the polynomial object
    poly, d0 = polyfit(dates, levels, p)

    #plot the graphs
    plt.plot(dates, levels, label="water level")
    plt.plot(dates, poly(dates_float - dates_float[0]), label="water level fit")
    plt.axhline(y=station.typical_range[0], color='b', linestyle='-', label="typical low")
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-', label="typical high")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()