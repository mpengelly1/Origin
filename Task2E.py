from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.datafetcher import fetch_level_list
import datetime

def run():
    # Build list of stations
    stations = build_station_list()
    level_list = fetch_level_list(stations, 1)
    print(level_list)
run()