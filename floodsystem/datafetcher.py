"""This module provides functionality for retrieving real-time and
latest time history level data

"""

import os
import json
import requests

import dateutil.parser
import datetime

from threading import Thread
from queue import Queue


def fetch(url):
    """Fetch data from url and return fetched JSON object"""
    r = requests.get(url)
    data = r.json()
    return data


def dump(data, filename):
    """Save JSON object to file"""
    f = open(filename, 'w')
    data = json.dump(data, f)


def load(filename):
    """Load JSON object from file"""
    f = open(filename, 'r')
    data = json.load(f)
    return data


def fetch_station_data(use_cache=True):
    """Fetch data from Environment agency for all active river level
    monitoring stations via a REST API and return retrieved data as a
    JSON object.

    Fetched data is dumped to a cache file so on subsequent call it
    can optionally be retrieved from the cache file. This is faster
    than retrieval over the Internet and avoids excessive calls to the
    Environment Agency service.

    """

    # URL for retrieving data for active stations with river level
    # monitoring (see
    # http://environment.data.gov.uk/flood-monitoring/doc/reference)
    url = "http://environment.data.gov.uk/flood-monitoring/id/stations?status=Active&parameter=level&qualifier=Stage&_view=full"

    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except:
        pass
    cache_file = os.path.join(sub_dir, 'station_data.json')

    # Attempt to load station data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except:
            # If load from file fails, fetch and dump to file
            data = fetch(url)
            dump(data, cache_file)
    else:
        # Fetch and dump to file
        data = fetch(url)
        dump(data, cache_file)

    return data


def fetch_latest_water_level_data(use_cache=False):
    """Fetch latest levels from all 'measures'. Returns JSON object"""

    # URL for retrieving data
    url = "http://environment.data.gov.uk/flood-monitoring/id/measures?parameter=level&qualifier=Stage&qualifier=level"

    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except:
        pass
    cache_file = os.path.join(sub_dir, 'level_data.json')

    # Attempt to load level data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except:
            data = fetch(url)
            dump(data, cache_file)
    else:
        data = fetch(url)
        dump(data, cache_file)

    return data


def fetch_measure_levels(measure_id, dt):
    """Fetch measure levels from latest reading and going back a period
    dt. Return list of dates and a list of values.

    """

    # Current time (UTC)
    now = datetime.datetime.utcnow()

    # Start time for data
    start = now - dt

    # Construct URL for fetching data
    url_base = measure_id
    url_options = "/readings/?_sorted&since=" + start.isoformat() + 'Z'
    url = url_base + url_options

    # Fetch data
    data = fetch(url)

    # Extract dates and levels
    dates, levels = [], []
    try:
        for measure in data['items']:
            # Convert date-time string to a datetime object
            d = dateutil.parser.parse(measure['dateTime'])

            # Append data
            dates.append(d)
            levels.append(measure['value'])

            return dates, levels
    except:
        return dates, 0

def fetch_level_list(stations, dt):
    'Multithreaded function to get level data for a list of station, outputs a list of tuples of id and level data'
    def thread0(state):
        print('Thread 0 started')
        level_list0 = list()
        for station in stations[:451]: #split workload
            level_list0.append(
                (station.measure_id, fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))))
        print('Thread 0 finished')

        return level_list0

    def thread1(state):
        print('Thread 1 started')
        level_list1 = list()
        for station in stations[451:901]: #split workload
            level_list1.append(
                (station.measure_id, fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))))
        print('Thread 1 finished')

        return level_list1

    def thread2(state):
        print('Thread 2 started')
        level_list2 = list()
        for station in stations[901:1351]: #split workload
            level_list2.append(
                (station.measure_id,fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))))
        print('Thread 2 finished')

        return level_list2

    def thread3(state):
        print('Thread 3 started')
        level_list3 = list()
        for station in stations[1351:]: #split workload
            level_list3.append(
                (station.measure_id, fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))))
        print('Thread 3 finished')

        return level_list3

    que = Queue()

    part_0 = Thread(target=lambda q, arg1: q.put(thread0(arg1)), args=(que, True))
    part_1 = Thread(target=lambda q, arg1: q.put(thread1(arg1)), args=(que, True))
    part_2 = Thread(target=lambda q, arg1: q.put(thread2(arg1)), args=(que, True))
    part_3 = Thread(target=lambda q, arg1: q.put(thread3(arg1)), args=(que, True))

    part_0.start()
    part_1.start()
    part_2.start()
    part_3.start()

    part_0.join()
    part_1.join()
    part_2.join()
    part_3.join()

    final_list = list()
    while not que.empty():
        result = que.get()
        final_list =+ result

    return final_list[1]