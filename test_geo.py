import pytest
import floodsystem

def test_stations_by_distance():
    stations = floodsystem.stationdata.build_station_list()
    list = floodsystem.geo.stations_by_distance(stations, (52.2053, 0.1218))

    #tests sort on list and distance
    assert list[0][0].name == "Cambridge Jesus Lock"
    assert list[0][1] == 0.8402364350834995

