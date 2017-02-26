from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    # Build list of stations

    stations = build_station_list()
    update_water_levels(stations)
    result = stations_level_over_threshold(stations, 0.8)

    for stations in result:
        print(stations[0], stations[1])

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")

    # Run Task2B
    run()
