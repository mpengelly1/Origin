import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    """computes a least-squares fit of polynomial of degree p
    to water level data. The function should return a tuple
    of (1) the polynomial object and (2) any shift of the time (date) axis"""

    # Find coefficients of best-fit polynomial
    t = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(t - t[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    matplotlib.pyplot.plot(t, levels, '.')

    # Plot polynomial fit at 30 points along interval
    t1 = np.linspace(t[0], t[-1], 30)
    plt.plot(t1, poly(t1-t[0]))