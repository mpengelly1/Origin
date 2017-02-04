from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river, rivers_with_station


def run():
    """Requirements for Task 1D"""

    #Build list of stations
    try:
        stations = build_station_list()
    except:
        raise RuntimeError('Failed to build list of stations')

    #Check all rivers are found by rivers_with_station
    rivers = rivers_with_station(stations)  # create set of all rivers
    assert len(rivers) > 800
    print('total number of rivers is ', len(rivers))

    #create and test list of 10 first rivers
    rivers_list = list(rivers)
    rivers_list.sort()
    assert rivers_list[0] == 'Addlestone Bourne'
    assert rivers_list[-1] == 'Yeading Brook West'
    print('first 10 rivers are:\n', rivers_list[:10],'\n')

    #Test stations_by_river function
    River_Aire = list(stations_by_river(stations)['River Aire'])
    River_Aire.sort()
    assert River_Aire[0] == 'Airmyn'
    assert River_Aire[-1] == 'Stockbridge'
    print('Stations on River Aire:\n',River_Aire,'\n')

    River_Cam = list(stations_by_river(stations)['River Cam'])
    River_Cam.sort()
    assert River_Cam[0] == 'Cam'
    assert River_Cam[-1] == 'Weston Bampfylde'
    print('Stations on River Cam:\n', River_Cam, '\n')

    Thames = list(stations_by_river(stations)['Thames'])
    Thames.sort()
    assert Thames[0] == 'Abingdon Lock'
    assert Thames[-1] == 'Windsor Park'
    print('Stations on River Thames:\n', Thames, '\n')


run()
