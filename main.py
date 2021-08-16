# Ishmael Martin
# ID: 001079482

import csv_reader
import dispatch
import models
import util
import re

package_hash_table = csv_reader.convert_cvs_to_hashtable()
address_hash_table = csv_reader.address_registry_cvs_to_hashtable()
delivered_packages = []


def report_delivered_packages(load):
    """
    Puts all delivered packages into a delivered package list.
    Runtime is O(n).
    Parameters
    ----------
    load : list
        list of packages
    """
    for package in load:
        delivered_packages.append(package)


def look_up(user_choice):
    """
    Takes the user choice and looks up the package or packages based on their choice.
    The runtime is O(n).

    Parameters
    ----------
    user_choice : str
        the user choice
    """
    if user_choice == "Package ID":
        while True:
            try:
                # user input of the package ID that the user wants to look up
                user_input: int = int(input("Enter Package ID: "))

                # package object of the ID entered
                found_package = None
                for package in delivered_packages:
                    if package.package_id == user_input:
                        found_package = package

                if found_package is not None:
                    print("*************************")
                    print(found_package)
                    break

                # is triggered if the ID entered does not correspond to a package
                else:
                    print("You entered a package ID that does not exist. Please try again.")

            # an exception that is triggered if the package ID is not a integer
            except ValueError:
                print('You did not enter a invalid package ID!')

    if user_choice == "Delivery Address":
        print('Enter number corresponding address: \n')
        for address_id in range(27):
            address = address_hash_table.search(address_id).address
            print(str(address_id) + ' - ' + address)

        while True:
            try:
                # user input of the package ID that the user wants to look up
                user_input: int = int(input("Enter address ID: "))

                # list of packages that was delivered to address selected
                found_packages = []
                for package in delivered_packages:
                    if package.address_id == user_input:
                        found_packages.append(package)

                if found_packages:
                    print("*************************")
                    for package in found_packages:
                        print(package)
                        print("*************************")
                    break

                # is triggered if the ID entered does not correspond to a package
                else:
                    print("You entered a Address ID that does not exist. Please try again.")

            # an exception that is triggered if the package ID is not a integer
            except ValueError:
                print('You did not enter a invalid Address ID!')

    if user_choice == "Delivery Deadline":
        while True:
            # user input of the package ID that the user wants to look up
            user_input = input("Enter delivery deadline to look up (HH:MM PM or AM): ")

            # regex pattern to check if the user input is in valid format
            pattern = '[0-9][0-9]:[0-9][0-9] [AP][M]'
            check = re.match(pattern, user_input)

            if check is None:
                print('You did not enter a valid delivery deadline!')
            else:
                sorted_packages = util.filter_packages(delivered_packages, user_input)

                # delivered
                print('*******************************')
                print('* Packages that was delivered *')
                print('*******************************')
                for package in sorted_packages[2]:
                    package_info = ("Package ID: {package.package_id} | "
                                    # "Delivery Address: {address}\n"
                                    "Delivery Deadline: {package.delivery_deadline} | "
                                    "Package Weight: {package.weight} | "
                                    "Delivery Status: delivered | "
                                    "Delivered Time: {package.delivered_time}").format(package=package)

                    print(package_info)

                # en_route
                print('*********************')
                print('* Packages in route *')
                print('*********************')
                for package in sorted_packages[1]:
                    package_info = ("Package ID: {package.package_id} | "
                                    # "Delivery Address: {address}\n"
                                    "Delivery Deadline: {package.delivery_deadline} | "
                                    "Package Weight: {package.weight} | "
                                    "Delivery Status: en route | "
                                    "Delivered Time: {package.delivered_time}").format(package=package)

                    print(package_info)

                # at_the_hub
                print('***********************')
                print('* Packages at the Hub *')
                print('***********************')
                for package in sorted_packages[0]:
                    package_info = ("Package ID: {package.package_id} | "
                                    # "Delivery Address: {address}\n"
                                    "Delivery Deadline: {package.delivery_deadline} | "
                                    "Package Weight: {package.weight} | "
                                    "Delivery Status: at the Hub | "
                                    "Delivered Time: {package.delivered_time}").format(package=package)

                    print(package_info)
                break
    if user_choice == "Delivery City":
        cities = []
        city_id = 1
        print('Enter number corresponding to the city: ')
        for package in delivered_packages:
            package_city = package.city
            if package_city not in cities:
                cities.append(package.city)
                print(str(city_id) + ' - ' + package.city)
                city_id += 1

        while True:
            try:
                # user input of the package ID that the user wants to look up
                user_input: int = int(input("Enter ciy ID: "))

                # package object of the ID entered
                if user_input not in range(1, len(cities) + 1):
                    continue
                found_packages = []
                for package in delivered_packages:
                    if package.city == cities[user_input - 1]:
                        found_packages.append(package)

                if found_packages:
                    for package in found_packages:
                        print("*************************")
                        print(package)
                    break

                # is triggered if the city entered does not correspond to a package
                else:
                    print("No package was delivered in the city entered")

            # an exception that is triggered if the package ID is not a integer
            except ValueError:
                print('You did not enter a invalid city ID!')

    if user_choice == "Delivery Zip Code":

        while True:
            try:
                # user input of the package zip code that the user wants to look up
                user_input: int = int(input("Enter zip code: "))

                # package object of the ID entered
                found_packages = []
                for package in delivered_packages:
                    if package.zip_code == str(user_input):
                        found_packages.append(package)

                if found_packages:
                    for package in found_packages:
                        print("*************************")
                        print(package)
                    break

                # is triggered if the zip code entered does not correspond to a package
                else:
                    print("No package was delivered in the zip code entered")

            # an exception that is triggered if the zip code is not a integer
            except ValueError:
                print('You did not enter a invalid zip code!')

    if user_choice == "Package Weight":
        while True:
            try:
                # user input of the package weight that the user wants to look up
                user_input: int = int(input("Enter zip code: "))

                # list of packages with of the weight entered
                found_packages = []
                for package in delivered_packages:
                    if package.weight == str(user_input):
                        found_packages.append(package)

                if found_packages:
                    for package in found_packages:
                        print("*************************")
                        print(package)
                    break

                # is triggered if the weight entered does not correspond to a package
                else:
                    print("No package was delivered in the zip code entered")

            # an exception that is triggered if the weight is not a integer
            except ValueError:
                print('You did not enter a invalid weight!')
    if user_choice == "Delivery status":

        # the 3 possible statuses a package can have
        statuses = ['at the hub', 'en route', 'delivered']

        status_id = 1
        print("Enter the status id that corresponds to the status you want to look up: ")
        for status in statuses:
            print(str(status_id) + ' - ' + status)
            status_id += 1

        while True:
            try:
                # user input of the package status that the user wants to look up
                user_input: int = int(input("Enter status id: "))

                if user_input not in range(1, len(statuses) + 1):
                    continue

                # list of packages with of the status entered
                found_packages = []
                for package in delivered_packages:
                    if package.status == statuses[user_input - 1]:
                        found_packages.append(package)

                if found_packages:
                    for package in found_packages:
                        print("*************************")
                        print(package)
                    break

                # is triggered if the status selected does not correspond to a package
                else:
                    print("No package has that status")

            # an exception that is triggered if the weight is not a integer
            except ValueError:
                print("You did not enter a invalid status code!")

    if user_choice == "Quit":
        exit()


def menu():
    """
    Proves a menu for the user. The Runtime of this function is O(n).
    """
    menu_options = ["Package ID", "Delivery Address", "Delivery Deadline", "Delivery City", "Delivery Zip Code",
                    "Package Weight",
                    "Delivery status", "Quit"]
    greeting_message: str = 'Welcome to the WGUPS package tracking system.\nSelect a menu option by entering the number that\ncorrespond to that option.\n'
    print(greeting_message)

    index = 1
    for option in menu_options:
        print(str(index) + '-' + option)
        index += 1

    while True:
        try:
            user_input: int = int(input("Enter you selection: "))
            if user_input in range(1, len(menu_options) + 1):
                # look_up(menu_options[user_input - 1])
                break
            else:
                print('You did not enter a number that correspond with a menu option!')
        except ValueError:
            print('You did not enter a number!')
            print('cult')

    look_up(menu_options[user_input - 1])


if __name__ == "__main__":

    # Load 1
    load_manifest1 = [13, 14, 15, 16, 19, 20, 1, 37, 40, 21, 4, 26, 34, 29, 30, 2]
    load1 = util.gather_packages_for_load(load_manifest1)
    list_of_stops = dispatch.create_list_of_stops(load1)
    route1 = dispatch.create_route(list_of_stops)

    # Load 2
    load_manifest2 = [3, 36, 38, 6, 25, 28, 32, 31]
    load2 = util.gather_packages_for_load(load_manifest2)
    list_of_stops2 = dispatch.create_list_of_stops(load2)
    route2 = dispatch.create_route(list_of_stops2)

    # Load 3
    load_manifest3 = [5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39, 18]
    load3 = util.gather_packages_for_load(load_manifest3)
    list_of_stops3 = dispatch.create_list_of_stops(load3)
    route3 = dispatch.create_route(list_of_stops3)

    # create Truck Objects and load them the their first load and route
    truck1 = models.Truck(load1, route1)
    truck2 = models.Truck(load2, route2)

    # loads truck
    truck1.load_truck()
    truck2.load_truck(3900)

    # delivers the packages to their destination
    truck1.deliver_package()
    truck2.deliver_package()

    truck2.reload_truck(load3, route3)
    truck2.deliver_package()

    report_delivered_packages(truck1.load)
    report_delivered_packages(truck2.load)

    print('Miles traveled')
    print(truck1.miles_traveled + truck2.miles_traveled)

    menu()
