from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    cambridge_coord = (52.2053, 0.1218)
    stations_by_dist = stations_by_distance(stations, cambridge_coord)

    # Build list of nearest stations
    nearest_stations = []
    for station, d in stations_by_dist[:10]:
        nearest_stations.append((station.name, station.town, d))

    print(nearest_stations)

    #Build list of furthest stations
    furthest_stations = []
    for station, d in stations_by_dist[-10:]:
        furthest_stations.append((station.name, station.town, d))

    print (furthest_stations)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")

    # Run Task1B
    run()
