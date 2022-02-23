import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    '''This function takes in a MonitoringStation object, 
    a dates list and a levels list, and plot a graph of past
    water levels against dates.'''


    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    return True