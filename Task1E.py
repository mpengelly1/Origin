from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list





def run():
    # Build list of stations
    stations = build_station_list()

    #output demonstration
    river_test = rivers_by_station_number(stations, 9)
    print(' The top 11 rivers with the most stations are: \n',river_test)

run()