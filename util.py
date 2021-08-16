import datetime


def calculate_time(time_delta):
    """
    Calculates the change in time.
    The runtime is O(1).

    Parameters
    ----------
    time_delta : int
        the change in time in seconds
            
    Return
    ------
    time : datetime object
        calculated time
    """
    # the start time
    clock = datetime.datetime(2021, 4, 6, 8)

    # the new time
    time = clock + datetime.timedelta(0, time_delta)
    return time.strftime("%I:%M %p")


def gather_packages_for_load(package_list):
    import csv_reader
    package_hash_table = csv_reader.convert_cvs_to_hashtable()
    """
    Gathers package objects base on a list of package IDs passed.
    The runtime is O(n).

    Parameters
    ----------
    package_list : list
        A list of package IDs

    Return
    ------
    load : list
        A list of package objects
    """

    load = []
    for package_id in package_list:
        package = package_hash_table.search(package_id)

        load.append(package)
    return load


def convert_time(time: str):
    """

    Converts time string and converts it into and returns in datetime object

    Parameters
    ----------
    time : str
        time in HH:MM AM/PM format

    Returns
    -------
    time_object : object
        datetime object
    """
    if len(time) == 7:
        time = '0{0}'.format(time)
    hour_str = "{0}{1}".format(time[0], time[1])
    minute_str = "{0}{1}".format(time[3], time[4])
    period = "{0}{1}".format(time[6], time[7])
    # format = '%I:%M %p'

    if period == 'PM':
        if hour_str != '12':
            hour = int(hour_str) + 12
        else:
            hour = int(hour_str)
        minute = int(minute_str)
        time_object = datetime.time(hour, minute)
        return time_object
    else:
        hour = int(hour_str)
        minute = int(minute_str)
        time_object = datetime.time(hour, minute)
        return time_object


def filter_packages(load, delivery_time):
    """

    Filter packages and sorts them by their status at a Specific time

    Parameters
    ----------
    load : list
        list of packages

    delivery_time : str
        time to filter packages by

    Returns
    -------
    sorted_packages : list
        a list sorted packages categorized in list

    """
    at_the_hub = []
    en_route = []
    delivered = []

    for package in load:
        if convert_time(package.delivered_time) <= convert_time(delivery_time):
            delivered.append(package)
        elif convert_time(package.loaded_time) <= convert_time(delivery_time):
            en_route.append(package)
        else:
            at_the_hub.append(package)
    sorted_packages = [at_the_hub, en_route, delivered]
    return sorted_packages


def calculate_time_traveled(miles_traveled):
    """
    Calculated the amount of time it took to travel the miles_traveled.
    The runtime is O(1).

    Parameters
    ----------
    miles_traveled : float
        The total amount of miles the truck traveled

    Returns
    -------
    time_traveled : int
        Time it took to travel the miles_traveled
    """
    speed = 18
    time_traveled = (miles_traveled / speed) * 3600.00
    return time_traveled




