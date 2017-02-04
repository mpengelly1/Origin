from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


#Build list of stations
try:
        stations = build_station_list()
except:
        raise RuntimeError('Failed to build list of stations')


def run():

    river_test = rivers_by_station_number(stations, 9)
    unique_values = {river_test[river][1] for river in range(len(river_test))}
    assert len(unique_values) == 9
    print(' The top 11 rivers with the most stations are: \n',river_test)

run()