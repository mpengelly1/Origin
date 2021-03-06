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
    level_list = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() is not None]

    #sort by current level
    level_list.sort(key=lambda x: x[1], reverse=True)

    #plot top 5 stations
    dt = 10
    for station in level_list[:5]:
        #get level history for each station
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))

        # Remove None values
        for date in dates:
            if date is None:
                levels.remove(levels[dates.index(date)])
                dates.remove(date)

        for level in levels:
            if level is None:
                dates.remove(dates[levels.index(level)])
                levels.remove(level)

        plot_water_levels(station[0],dates,levels)

run()
