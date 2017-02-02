from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river, rivers_with_station


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    try:
        stations = build_station_list()
    except:
        raise RuntimeError('Failed to build list of stations')


    rivers = rivers_with_station(stations)  # create set of all rivers
    assert len(rivers) == 843

    print('total number of rivers is ', len(rivers))
    rivers_list = list(rivers)
    rivers_list.sort()
    assert rivers_list[:10] == ['Addlestone Bourne', 'Adur', 'Aire Washlands', 'Alconbury Brook',
 'Aldbourne', 'Aller Brook', 'Alre', 'Alt', 'Alverthorpe Beck', 'Ampney Brook']
    print('first 10 rivers are: ', rivers_list[:10])


run()
