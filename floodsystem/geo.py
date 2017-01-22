"""This module contains a collection of functions related to
geographical data.

"""


#Import modules from other files
from .utils import sorted_by_key
from .station import MonitoringStation


def rivers_with_station(stations):
  "Given a list of stations, returns all rivers (by name) with a monitoring station. Returns rivers as a set."
  
  
def stations_by_river(stations):
  "Assigns rivers as keys to stations specified within a python dict."
  
  {station.river : station.name for station in stations}  #Sets rive
