from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from datetime import datetime, timedelta
import matplotlib.pyplot as plt



def run():
    # Build list of stations
    stations = build_station_list()

    #generate list of levels, filtering out 'None' levels
    update_water_levels(stations)
    level_list = [(station ,station.relative_water_level()) for station in stations if station.relative_water_level() is not None]

    #sort by current level
    level_list.sort(key=lambda x: x[1], reverse=True)

    #plot top 5 stations
    dt = 2   #get 2 days of data

    N=5
    for station in level_list[:N]:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))

        #Remove None values
        for date in dates:
            if date is None:
                levels.remove(levels[dates.index(date)])
                dates.remove(date)

        for level in levels:
            if level is None:
                dates.remove(dates[levels.index(level)])
                levels.remove(level)

        #plot
        try:
            plot_water_level_with_fit(station[0], dates, levels, 4)
        except:
            N+=1
            continue


    plot_water_level_with_fit(stations[0],dates,levels,4)

run()
