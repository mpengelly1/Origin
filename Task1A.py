from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    try:
        stations = build_station_list()
    except:
        raise RuntimeError('Failed to build list of stations')

    # Count number of stations and print
    print("Number of stations: {}".format(len(stations)))

    # Display data from 3 stations:
    for station in stations:
        if station.name in ['Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge']:
            print(station)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
