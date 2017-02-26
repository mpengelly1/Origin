from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

def run():
    # Build list of stations

    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    result = flood.stations_highest_rel_level(stations, N)

    print(result)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    # Run Task2B
    run()
