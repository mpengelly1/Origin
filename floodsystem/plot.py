import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels, display = True):
     'Plots water level against time. Accepts dates and levels as a list'

     # Plot
     plt.plot(dates, levels)

     # Add axis labels, rotate date labels and add plot title
     plt.xlabel('date')
     plt.ylabel('water level (m)')
     plt.xticks(rotation=45);
     plt.title(station.name)

     # Display plot if required
     plt.tight_layout()  # This makes sure plot does not cut off date labels
     if display == True:
         plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
     'plots the water level data and the best-fit polynomial. '

     plot_water_levels( station , dates , levels, False)
     polyfit(dates,levels,p)
     plt.plot(dates,np.linspace(1,1,len(dates))*station.typical_range[0])
     plt.plot(dates, np.linspace(1, 1, len(dates)) * station.typical_range[1])
     plt.show()