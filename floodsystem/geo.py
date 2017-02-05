"""This module contains a collection of functions related to
geographical data.

"""

# Import modules from other files
from .utils import sorted_by_key
from .station import check_station_input
from .haversine import haversine


def rivers_with_station(stations):
    "Given a list of stations, returns all rivers (by name) with a monitoring station. Returns rivers as a set."

    check_station_input(stations)
    return {station.river for station in stations}  # enters all rivers into a set

  
def stations_by_river(stations):
    "Assigns rivers as keys to stations specified within a python dict containing lists."

    check_station_input(stations)
    river_dict = dict() #Create dictionary to store output
    for station in stations: #Add new entry if key is not found, or append to list if it is
        if station.river in river_dict:
            river_dict[station.river].append(station.name)
        else:
            river_dict[station.river] = [station.name]
    return river_dict #return dict of lists

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring stations.
    Returns list of tuples sorted by number of stations"""

    #Checks input
    check_station_input(stations)
    if type(N) != int:
        raise TypeError('input was not an integer')
    if N > len(stations):
        raise ValueError('not enough stations for the top N rivers to be found')
    if N < 1:
        raise ValueError("number of rivers should be greater than or equal to 1")

    #sort rivers into order by number of stations
    river_dict = stations_by_river(stations)
    rivers_by_N = sorted(river_dict, key=lambda k: len(river_dict[k]), reverse=True)
    river_list = [(river, len(river_dict[river])) for river in rivers_by_N]

    # keep adding rivers if their value is the same as the lowest included river
    min_len = river_list[N-1][1]
    while river_list[N][1] == min_len:
        N += 1
        if river_list[N][1] == min_len:
            N += 1
            break
    return river_list[:N]



def stations_by_distance(stations, p):
    """Sorts stations by distance. Stations is a list of stations, p is a tuple (latitude, longitude).
    The function returns a list of tuples (station, distance)"""

    #check input
    check_station_input(stations)
    if p != tuple:
        raise TypeError('Please enter a tuple with coordinates')
    elif len(p) != 2:
        raise ValueError('Please enter a coordinate')

    station_distance = []

    for s in stations:
        #s.coord
        distance = haversine(s.coord, p)
        station_distance.append((s, distance))

    return sorted_by_key(station_distance, 1)

def stations_within_radius(stations, centre, r):
    """sorts stations into distance and lists stations within a certain radius. Stations is a list of stations,
    centre is a coordinate which should be taken as the centre of a circle, and r is the distance in km in which the
    stations have to be from the centre of the circle."""

    #Check input
    check_station_input(stations)
    if centre != tuple:
        raise TypeError('Please enter a tuple with coordinates')
    elif len(centre) != 2:
        raise ValueError('Please enter a coordinate')
    if r != float or int
        raise TypeError('please enter a valid distance in km')

    station_rad = []

    for s in stations:
        # s.coord
        distance = haversine(s.coord, centre)
        if distance < r:
            station_rad.append(s.name)

    return sorted_by_key(station_rad, 0)