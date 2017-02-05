from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river, rivers_with_station


def run():
    """Requirements for Task 1D"""

    stations = build_station_list()


    #Check all rivers are found by rivers_with_station
    rivers = rivers_with_station(stations)  # create set of all rivers
    print('total number of rivers is ', len(rivers))

    #create and test list of 10 first rivers
    rivers_list = list(rivers)
    rivers_list.sort()
    print('first 10 rivers are:\n', rivers_list[:10],'\n')

    #Test stations_by_river function
    River_Aire = list(stations_by_river(stations)['River Aire'])
    River_Aire.sort()
    print('Stations on River Aire:\n',River_Aire,'\n')

    River_Cam = list(stations_by_river(stations)['River Cam'])
    River_Cam.sort()
    print('Stations on River Cam:\n', River_Cam, '\n')

    Thames = list(stations_by_river(stations)['Thames'])
    Thames.sort()
    print('Stations on River Thames:\n', Thames, '\n')


run()
