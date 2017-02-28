from .utils import sorted_by_key
from floodsystem import station, flood


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

    ordered_stations_list = sorted(station_list, key=lambda x: x[1], reverse = True)
    return ordered_stations_list[:N]
