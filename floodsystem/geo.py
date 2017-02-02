"""This module contains a collection of functions related to
geographical data.

"""

# Import modules from other files
from .utils import sorted_by_key
from .station import MonitoringStation


def rivers_with_station(stations):
    "Given a list of stations, returns all rivers (by name) with a monitoring station. Returns rivers as a set."

    if type(stations) != list:
        raise TypeError('input was not a list of stations')
    return {station.river for station in stations}  # enters all rivers into a set


def stations_by_river(stations):
    "Assigns rivers as keys to stations specified within a python dict containing lists."

    if type(stations) != list: #checks type is valid
        raise TypeError('input was not a list of stations')
    river_dict = dict() #Create dictionary to store output
    for station in stations: #Add new entry if key is not found, or append to list if it is
        if station.river in river_dict:
            river_dict[station.river].append(station.name)
        else:
            river_dict[station.river] = [station.name]
    return river_dict #return dict of lists
