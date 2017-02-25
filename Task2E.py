from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels(measure_id, dt):

def run():
    # Build list of stations
    stations = build_station_list()
    stations_by_level = ((station.measure_id, fetch_measure_levels(station.measure_id,
                                                                   1) =datetime.timedelta(days=1))[-1] for station in stations])
    plot_water_levels ()
