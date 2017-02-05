"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """"Checks that stations do not have inconsistent data. checks the typical high/low range data for consistency.
         The method should return True if the data is consistent and False if the data is inconsistent or unavailable"""

        if self.typical_range == None:
            return False
        elif self.typical_range[1] < self.typical_range[0]:
            return False
        else:
            return True


def check_station_input(stations):
    if type(stations) != list:
        raise TypeError('input was not a list of stations')
    try:
        stations[1].river
    except Exception:
        print("ValueError: Please enter a list of stations")
    pass

def inconsistent_typical_range_stations(stations):
    "given a list of stations objects, returns a list of stations that have inconsistent data."
    check_station_input(stations)
    bad_stations = list()
    for station in stations:
        if station.typical_range_consistent() == False:
            bad_stations.append(station)
    return bad_stations
