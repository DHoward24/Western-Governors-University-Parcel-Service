import util


class Package:
    """
    A class to represent a package

    Attributes
    ----------
    package_id : str
        The id of the package

    address_id : str
        The id of the address of the package delivery destination

    city : str
        The city of the package delivery destination

    state: str
        The state of the package delivery destination

    zip_code : str
        the zip code of the package delivery destination

    delivery_deadline : str
        The time when the package needs to be delivered

    weight : str
        The weight of the package

    special_notes : str
        Special notes about the package delivery

    status : str
        The status of the package during the delivery package

    delivered_time : str
        The time when the package was delivered
    """

    def __init__(self, package_id, address_id, city, state, zip_code, delivery_deadline, weight, special_notes,
                 status='at the hub', loaded_time=None, delivered_time=None):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            package_id : str
                The id of the package

            address_id : str
                The id of the address of the package delivery destination

            city : str
                The city of the package delivery destination

            state: str
                The state of the package delivery destination

            zip_code : str
                the zip code of the package delivery destination

            delivery_deadline : str
                The time when the package needs to be delivered

            weight : str
                The weight of the package

            special_notes : str
                Special notes about the package delivery

            status : str
                The status of the package during the delivery package

            delivered_time : str
                The time when the package was delivered
        """
        self.package_id = package_id
        self.address_id = address_id
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
        self.loaded_time = loaded_time
        self.delivered_time = delivered_time

    def __str__(self):
        import csv_reader
        address = csv_reader.convert_address_id_to_address(int(self.address_id))
        statement = ("Package ID: {self.package_id}\n"
                     "Delivery Address: {address}\n"
                     "Delivery Deadline: {self.delivery_deadline} \n"
                     "Delivery City: {self.city}\n"
                     "Delivery Zip: {self.zip_code}\n"
                     "Package Weight: {self.weight} \n"
                     "Delivery Status: {self.status}\n"
                     "Delivered Time: {self.delivered_time}").format(self=self, address=address.address)

        return statement


class Destination:
    """
    A class to represent a destination

    Attributes
    ----------
    destination_id : str
        The id of the destination

    destination_name : str
        The name of the destination

    destination_address : str
        the address of the destination
    """

    def __init__(self, destination_id, destination_name, destination_address):
        self.destination_ID = destination_id
        self.name = destination_name
        self.address = destination_address


class Truck:
    """
    A class to represent a Delivery Truck

    Attributes
    ----------
    load : list
        A list of package that the truck need to delivery

    route : list
        The list of stops the truck needs to travel to in order

    miles_traveled : float
        The total amount of miles the truck traveled

    speed : int
        The speed of the truck

    Methods
    -------
    add_miles_traveled(miles: float):
        Adds miles to the truck's miles_traveled attribute

    calculate_time_traveled(miles_traveled):
        Calculated the amount of time it took to travel the miles_traveled

    reload_truck(load, route):
        reloads truck with a new load and route if the truck has another load to delivery

    deliver_package():
        delivers all the packages in the load to their destination

    load_truck(load):
        Once the load is on the truck, the packages status are changed
    """

    def __init__(self, load, route):
        """
        Constructs all the necessary attributes for the truck object.

        Parameters
        ----------
        load : list
            List of packages

        route : list
            List of stops the truck has to deliver packages to in order
        """
        self.load = load
        self.route = route
        self.miles_traveled = 0.0
        self.total_time_traveled = 0.0
        self.first_route_time_traveled = 0.0
        self.speed = 18

    def add_miles_traveled(self, miles: float):
        """
        Adds miles to the truck's miles_traveled attribute.
        The runtime is O(1)

        Parameters
        ----------
        miles : float
            miles traveled to add to total
        """
        self.miles_traveled += miles

    def load_truck(self, time=None):

        """
        Changes the status  of packages in the load to en route
        """
        if time is not None:
            self.total_time_traveled = time

        for package in self.load:
            package.status = 'en route'
            package.loaded_time = util.calculate_time(self.total_time_traveled)

    def reload_truck(self, load, route):
        """
        Reloads truck with a new load and route if the truck has another load to delivery.
        The runtime is O(n).

        Parameters
        ----------
        load : list
            A list of package that the truck need to delivery

        route : list
            The list of stops the truck needs to travel to in order
        """
        self.route = route
        self.first_route_time_traveled = self.total_time_traveled

        for package in load:
            package.loaded_time = util.calculate_time(self.total_time_traveled)
            package.status = 'en route'
            self.load.append(package)

    def deliver_package(self):
        """
        Delivers all the packages in the load to their destination.
        """
        # import csv_reader inside method to avoid circular import error
        import csv_reader

        # the hub
        hub = 0

        # current location of truck
        current_location = 0

        for stop in self.route:

            # calculates the distance between the current location and next stop
            distance_traveled = float(csv_reader.distance_lookup(current_location, stop))

            # adds distance traveled to truck total miles traveled
            self.miles_traveled += distance_traveled

            # calculates time travel
            time_traveled = util.calculate_time_traveled(distance_traveled)

            # adds time traveled to total time traveled
            self.total_time_traveled += time_traveled

            # the stop becomes the current location of the truck
            current_location = stop

            for package in self.load:
                if package.status != 'delivered' and package.address_id == current_location:
                    # sets the package status to delivered
                    package.status = 'delivered'

                    # sets the package delivery time
                    package.delivered_time = util.calculate_time(self.total_time_traveled)

            # checks if the truck is at the last stop of the delivery route
            if current_location == self.route[len(self.route) - 1]:
                # calculates the distance between the last stop and the hub
                distance_traveled = float(csv_reader.distance_lookup(current_location, hub))

                # adds distance traveled to truck total miles traveled
                self.miles_traveled += distance_traveled

                # calculates time travel
                time_traveled = util.calculate_time_traveled(distance_traveled)

                # adds time traveled to total time traveled
                self.total_time_traveled += time_traveled

