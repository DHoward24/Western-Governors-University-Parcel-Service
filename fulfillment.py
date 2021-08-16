import csv_reader

table = csv_reader.convert_cvs_to_hashtable()


def gather_packages_for_load(load_list):
    """
    Gathers package objects base on a list of package IDs passed.
    The runtime is O(n).

    Parameters
    ----------
    load_list : list
        A list of package IDs

    Return
    ------
    load : list
        A list of package objects
    """

    load = []
    for package_id in load_list:
        package = table.search(package_id)
        load.append(package)
    return load

