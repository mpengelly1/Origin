from .utils import sorted_by_key


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




    return sorted_by_key(output, 1, False)

