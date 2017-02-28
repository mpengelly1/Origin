from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
import matplotlib.dates
import matplotlib.pyplot as plt
import numpy as np


def stations_level_over_threshold(stations, tol):
    output = []

    for station in stations:
            #if station.relative_water_level() is None:
          #  pass
        try:
            if station.relative_water_level() > tol:
                output.append((station.name, station.relative_water_level()))
        except:
            pass

    result = sorted_by_key(output, 1, False)
    return result


def stations_highest_rel_level(stations, N):
    station_list = []

    for station in stations:
         if station.relative_water_level() is not None:
            station_list.append((station.name, station.relative_water_level()))
         else:
            pass

    ordered_stations_list = sorted(station_list, key=lambda x: x[1], reverse=True)
    return ordered_stations_list[:N]

def risk_level(stations , anxiety = 1):
    """prints stations in order of decreasing risk, categorises based on current relative level,
     and rate of change of water level (weighted). Anxiety level can be set to make the categorisation
     more sensitive to risk"""

    risk_list = list()

    # generate list of levels, filtering out 'None' levels
    update_water_levels(stations)
    level_list = [(station, station.latest_level) for station in stations if station.latest_level is not None]

    for station in stations:
        dt = 3
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

        # Remove None values
        for date in dates:
            if date is None:
                levels.remove(levels[dates.index(date)])
                dates.remove(date)

        for level in levels:
            if level is None:
                dates.remove(dates[levels.index(level)])
                levels.remove(level)

        try:

            # Find coefficients of best-fit polynomial
            t = matplotlib.dates.date2num(dates)
            p_coeff = np.polyfit(t - t[0], levels, 4)

            # Convert coefficient into a polynomial that can be evaluated
            poly = np.poly1d(p_coeff)

            #calculate current gradient of polyfit
            derivative = poly.deriv()
            rate_of_change = derivative(t[-1])

            #Calculate risk factor, limiting derivative factor
            if -4 <= rate_of_change <= 4:
                risk = anxiety*(station.relative_water_level()) + 0.25*rate_of_change
            elif rate_of_change < -4:
                risk = anxiety*(station.relative_water_level() - 1)
            else:
                risk = anxiety*(station.relative_water_level() + 1)

            #sort stations into risk categories
            if risk < 1:
                category = 'low'
            elif 1 <= risk < 2:
                category = 'moderate'
            elif 2 <= risk < 3:
                category = 'high'
            else:
                category = 'severe'

            risk_list.append((station, risk, category))

        except:
            print('insufficient data for', station.name)
            continue

    risk_list.sort(key=lambda x: x[1], reverse=True)
    return risk_list
