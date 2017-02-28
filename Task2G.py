from floodsystem.flood import risk_level
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta, datetime
from floodsystem.plot import plot_water_level_with_fit


def run():

    # Build list of stations
    stations = build_station_list()

    #Categorise risk
    risk_list = risk_level(stations[:100],0.8)

    #Print top 10 most at risk
    for station in risk_list[:10]:
        print(station[0].name, station[2])

    #Plot most at risk
    dt = 3
    dates, levels = fetch_measure_levels(risk_list[0][0].measure_id, dt=timedelta(days=dt))
    plot_water_level_with_fit(risk_list[0][0], dates, levels, 4)



run()
