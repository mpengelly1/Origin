import floodsystem.station
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""

    #Build list of stations
    try:
        stations = build_station_list()
    except:
        raise RuntimeError('Failed to build list of stations')

    #Generate, sort and print list of inconsistent stations
    bad_stations = floodsystem.station.inconsistent_typical_range_stations(stations)
    bad_stations_names = [station.name for station in bad_stations]
    bad_stations_names.sort()
    print(bad_stations_names)

run()
