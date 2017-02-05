import floodsystem.stationdata
import floodsystem.geo
import floodsystem.station

#Build list of stations for tests
stations = floodsystem.stationdata.build_station_list()

def test_stations_by_distance():
    list = floodsystem.geo.stations_by_distance(stations, (52.2053, 0.1218))

    #tests sort on list and distance
    assert list[0][0].name == "Cambridge Jesus Lock"
    assert list[0][1] == 0.8402364350834995

def test_stations_within_radius():
    list = floodsystem.geo.stations_within_radius(stations, (52.2053, 0.1218), 10)

    assert "Bin Brook" in list

def test_rivers_by_station():
    river_test = floodsystem.geo.rivers_by_station_number(stations, 9)
    unique_values = {river_test[river][1] for river in range(len(river_test))}
    assert len(unique_values) == 9

def test_rivers_with_station():
    rivers = floodsystem.geo.rivers_with_station(stations)  # create set of all rivers
    assert len(rivers) > 800

    rivers_list = list(rivers)
    rivers_list.sort()
    assert rivers_list[0] == 'Addlestone Bourne'
    assert rivers_list[-1] == 'Yeading Brook West'

    River_Aire = list(floodsystem.geo.stations_by_river(stations)['River Aire'])
    River_Aire.sort()
    assert River_Aire[0] == 'Airmyn'
    assert River_Aire[-1] == 'Stockbridge'

    River_Cam = list(floodsystem.geo.stations_by_river(stations)['River Cam'])
    River_Cam.sort()
    assert River_Cam[0] == 'Cam'
    assert River_Cam[-1] == 'Weston Bampfylde'

    Thames = list(floodsystem.geo.stations_by_river(stations)['Thames'])
    Thames.sort()
    assert Thames[0] == 'Abingdon Lock'
    assert Thames[-1] == 'Windsor Park'

def test_inconsistent_typical_range():
    bad_stations = floodsystem.station.inconsistent_typical_range_stations(stations)
    assert len(bad_stations) > 2
    for station in bad_stations:
        assert station.typical_range == None or station.typical_range[0] > station.typical_range[1]

def run():
    test_rivers_by_station()
    test_stations_by_distance()
    test_stations_within_radius()
    test_rivers_with_station()
    test_inconsistent_typical_range()
    print("geo tests completed successfully")

run()