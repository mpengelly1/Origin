import floodsystem.utils
import floodsystem.station
import floodsystem.stationdata
from floodsystem import flood


def test_stations_level_over_threshold():

    s_id1 = "test-s-id1"
    m_id1 = "test-m-id1"
    label1 = "some station1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "River X"
    town1 = "My Town"
    s = floodsystem.station.MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
    s.latest_level = 3.4445

    s_id2 = "test-s-id2"
    m_id2 = "test-m-id2"
    label2 = "some station2"
    coord2 = (-5.0, 4.0)
    trange2 = (-2.3, 3.4445)
    river2 = "River X"
    town2 = "Your Town"
    t = floodsystem.station.MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    t.latest_level = -2.3

    output = flood.stations_level_over_threshold([s, t], 0.5)
    #print(output)

    assert ("some station1", 1.0) in output
    assert ("some station2", -2.3) not in output

test_stations_level_over_threshold()