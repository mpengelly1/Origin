from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    for station in stations:
        output = []

        if station.relative_water_level() is None:
            pass
        else:
            if station.relative_water_level() > tol:
                output.append((station.name, station.relative_water_level()))

    return sorted_by_key(output, 1, False)

