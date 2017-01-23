"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key

from haversine import haversine

def stations_by_distance(stations, p):
    """Sorts stations by distance. Stations is a list of stations, p is a tuple (latitude, longitude).
    The function returns a list of tuples (station, distance)"""

    station_distance = []

    for s in stations:
        #s.coord
        distance = haversine(s.coord, p)
        station_distance.append((s, distance))

    return sorted_by_key(station_distance, 1)
