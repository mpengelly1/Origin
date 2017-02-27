from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
import datetime

def run():
    # Build list of stations
    stations = build_station_list()

    #generate list of levels, filtering out 'None' levels
    update_water_levels(stations)
    level_list = [(station,station.latest_level) for station in stations if station.latest_level is not None]

    #sort by current level
    level_list.sort(key = lambda x: x[1], reverse = True)

    #plot top 5 stations
    plot_data = list()
    dt = 10
    for station in level_list[:5]:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station[0],dates,levels)

run()