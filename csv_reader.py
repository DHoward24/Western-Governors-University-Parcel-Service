from __future__ import annotations
from hash_table import ChainingHashTable
import models
import csv


def convert_address_to_id(address):
    """
    It converts an address and return the address ID.
    The Runtime of this method is O(n).

    Parameters
    ----------
    address : str
        The address that needs to be converted into a ID

    Returns
    -------
    destination_id : str
        The id of the address that was passed
    """

    # the address hashtable
    addresses = address_registry_cvs_to_hashtable()

    # loops through all the  addresses in the hashtable
    for destination_id in range(41):
        if address == addresses.search(destination_id).address:
            return destination_id


def convert_address_id_to_address(address_id):
    """
    It converts an address id and return the address.
    The Runtime of this method is O(1).

    Parameters
    ----------
    address_id : int
        The address ID that needs to be converted into the address

    Returns
    -------
    address : str
        the address
    """

    # address hashtable
    addresses = address_registry_cvs_to_hashtable()

    # the address object of the address ID
    address = addresses.search(address_id)
    return address


def address_registry_cvs_to_hashtable():
    """
    This  method converts entries from csv file, then
    creates a Destination objects from those entries and append
    them to a list. The runtime is O(n).

    Return
    ------
    address_list : list
        List of Destination objects
    """

    # path to the file
    file_name = 'resources/address_registry.csv'

    # hashtable instance
    hash_table = ChainingHashTable()

    with open(file_name, newline='', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            destination_id = int(row[0])
            destination_name = row[1]
            destination_address = row[2]

            # the new destination object created for the csv file
            destination = models.Destination(destination_id, destination_name, destination_address)

            # inserts the destination object into the hashtable
            hash_table.insert(destination_id, destination)
    return hash_table


def convert_cvs_to_hashtable():
    """
    This  method converts entries from csv file, then
    creates a package objects from those entries and insert
    them into a hashtable. The runtime is O(n).

    Return
    ------
    hash_table : hashtable
        A hash table that consist of package objects
    """

    file_name = "resources/WGUPSPackageFile.csv"
    hash_table = ChainingHashTable()

    with open(file_name, newline='', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            package_id = int(row[0])
            address = row[1]
            address_id = convert_address_to_id(address)
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_deadline = row[5]
            weight = row[6]
            special_note = " "

            if len(row) == 8:
                special_note = row[7]

            package = models.Package(package_id, address_id, city, state, zip_code, delivery_deadline, weight,
                                     special_note)
            hash_table.insert(package_id, package)
    return hash_table


def distance_csv_to_hashtable():
    """
    This  method converts entries from csv file, then
    creates a Destination objects from those entries and append
    them to a list. The runtime is O(n).

    Return
    ------
    address_list : list
        List of Destination objects
    """

    # Read in csv file that is the mapping of distances between locations
    file = "resources/distance.csv"
    with open(file) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        read_csv = list(read_csv)
        return read_csv


def distance_lookup(from_location, to_location):
    """
    Looks up the distance between location.

    Parameters
    ----------
    from_location : int
        the start location

    to_location : int
        the end location

    Return
    ------
    distance : str
        the distance between the two location
    """
    table = distance_csv_to_hashtable()
    distance = table[from_location - 1][to_location - 1]
    if distance != '':
        return distance
    else:
        distance = table[to_location - 1][from_location - 1]
        assert isinstance(distance, object)
        return distance
