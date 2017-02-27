from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.datafetcher import fetch_level_list
import datetime

def run():
    # Build list of stations
    stations = build_station_list()
    level_list = fetch_level_list(stations, 1)

    sorted_levels = sorted(level_list, key = lambda x: x[1][1], reverse = True)
    print(sorted_levels[:5])
run()