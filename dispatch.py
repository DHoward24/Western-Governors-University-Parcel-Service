import itertools
import sys
import csv_reader


def determine_next_stop(current_location, stops):
    """
    Create the route for the truck to take to deliver packages.
    The runtime is O(n).

    Parameters
    ----------
    current_location : int
        the current location of truck

    stops : list
        list of stops remaining

    Return
    ------
    possible_stops : dictionary
        a dictionary of trips (key) and the distance of the trip (value)
    """
    possible_stop = {}
    for stop in stops:
        # calculates the distance between the current location and the next possible stop
        calculated_distance = csv_reader.distance_lookup(current_location, stop)

        # adds a key value pair of possible trip (a tuple) and the distance of that trip
        possible_stop[(current_location, stop)] = float(calculated_distance)
    return possible_stop


def create_route(stop_list):
    """
    Create the route for the truck to take to deliver packages.
    The runtime is O(n^2).

    Parameters
    ----------
    stop_list : list
        A list of stops to visit

    Return
    ------
    route : list
        A list of the route for the truck to take
    """
    delivery_route = []
    stop_list = stop_list
    current_location = 0
    shortest_distance = sys.maxsize
    shortest_trip = None

    while len(stop_list) != 1:
        # calculate possible next trips from current location
        possible = determine_next_stop(current_location, stop_list)

        for key, value in possible.items():
            if value < shortest_distance:
                shortest_trip = key
                shortest_distance = value

        # adds the shortest next stop to delivery route
        delivery_route.append(shortest_trip[1])

        # makes the next shortest stop the current location
        current_location = shortest_trip[1]

        # removes current location from stop list
        stop_list.remove(shortest_trip[1])

        # resets shortest_distance variable
        shortest_distance = sys.maxsize

    # adds last stop to delivery route
    delivery_route.append(stop_list[0])

    return delivery_route


def create_list_of_stops(packages):
    """
    Create a list of stops based on the destination of the packages.
    The runtime is O(n)

    Parameters
    ----------
    packages : list
        Sorted list of packages

    Return
    ------
    stop_list : list
        A list of address IDs
    """
    stop_list = []
    for package in packages:
        stop_list.append(package.address_id)

    # removes any duplicates in list
    stop_list = list(dict.fromkeys(stop_list))
    return stop_list


