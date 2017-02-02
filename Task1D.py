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
    assert len(rivers) == 843
    print('total number of rivers is ', len(rivers))

    #create and test list of 10 first rivers
    rivers_list = list(rivers)
    rivers_list.sort()
    assert rivers_list[:10] == ['Addlestone Bourne', 'Adur', 'Aire Washlands', 'Alconbury Brook',
 'Aldbourne', 'Aller Brook', 'Alre', 'Alt', 'Alverthorpe Beck', 'Ampney Brook']
    print('first 10 rivers are:\n', rivers_list[:10],'\n')

    #Test stations_by_river function
    River_Aire = list(stations_by_river(stations)['River Aire'])
    River_Aire.sort()
    assert River_Aire == ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Saltaire', 'Snaygill', 'Stockbridge']
    print('Stations on River Aire:\n',River_Aire,'\n')

    River_Cam = list(stations_by_river(stations)['River Cam'])
    River_Cam.sort()
    assert River_Cam == ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Weston Bampfylde']
    print('Stations on River Cam:\n', River_Cam, '\n')

    Thames = list(stations_by_river(stations)['Thames'])
    Thames.sort()
    assert Thames == ['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen', 'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock', 'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock', 'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock', 'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock', 'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading', 'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock', 'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock', 'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay', 'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']
    print('Stations on River Thames:\n', Thames, '\n')


run()
