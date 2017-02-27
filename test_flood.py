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
    assert ("some station2", 0.0) not in output

def test_stations_highest_rel_level():
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

    s_id3 = "test-s-id3"
    m_id3 = "test-m-id3"
    label3 = "some station3"
    coord3 = (-3.0, 4.0)
    trange3 = (-2.3, 3.4445)
    river3 = "River X"
    town3 = "My Town"
    u = floodsystem.station.MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    u.latest_level = 0.57225

    s_id4 = "test-s-id4"
    m_id4 = "test-m-id4"
    label4 = "some station4"
    coord4 = (-4.0, 4.0)
    trange4 = (-2.3, 3.4445)
    river4 = "River X"
    town4 = "Your Town"
    v = floodsystem.station.MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)
    v.latest_level = 9.189

    output = flood.stations_highest_rel_level([s, t, u, v], 2)
    #print(output)

    assert ('some station4', 2.0) in output
    assert ('some station1', 1.0) in output
    assert ('some station2', 0.0) not in output
    assert ('some station3', 0.5) not in output


test_stations_level_over_threshold()
test_stations_highest_rel_level()