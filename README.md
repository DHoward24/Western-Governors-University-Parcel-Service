# Core Algorithm Overview

###### Author: Ishmael Martin (001079482)

### Stated Problem

The purpose of this project is to create an algorithm for the Western Governors University Parcel Service (WGUPS) to determine the best route and delivery distribution for their Salt Lake City Daily Local Deliveries (DLD). Packages are currently not being delivered by their promised deadline and a more efficient and accurate solution is necessary. The Salt Lake City route is covered by three trucks, two drivers, and has a daily average of approximately 40 packages.

#### Assumptions:

The following are the constraints imposed on the WGUPS delivery service:

- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Trucks have an “infinite amount of gas” with no need to stop.
- Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
- Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
- There is up to one special note for each package.
- The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
- The package ID is unique; there are no collisions.
- No further assumptions exist or are allowed.

#### Restrictions

Each package may have **one** special requirement that must be addressed by the WGUPS. The following are possible restrictions that may be imposed on a given package:

- The package must be delivered with other packages.
- We refer to these packages as _linked_ packages in our algorithm.
- The package must be delivered by a specific truck.
- The package has a specific deadline by which it must be delivered.
- The package is delayed in arriving at the depot and will not be available for pickup until later in the day.

### Algorithm Overview

The core WGUPS Package Routing system utilizes the nearest neighbors algorithm to solve the routing problem.
The algorithm takes a list of stops that a truck needs to travel to and then orders that list in a way that the next stop is the shortest in distance from the starting point or previous stop in the list. This algorithm has
a time complexity of O(N<sup>2</sup>). The Worst-case performance is 1/2[log<sub>2</sub>n]+1/2.

The Packages were manually sorted into 3 different loads to meet the requirements of the special notes of a package.
After a route is created for each load, a load and the corresponding route are put into a truck instance and start on the route. Whatever
truck makes it back to the starting location, the hub first takes the last load and route and delivers it. The total miles traveled
by all the trucks is 121.8 miles which meet the 140 miles limit. all packages were delivered on time, Even packages that
were not permitted to be delivered until 9:05 am because of a delay.

### Algorithm Pseudocode
```
list_of_stops = a list of stops that the truck needs to travel to 
route = list of stops in order

shortest_trip_distance = large number
shortest_destination = None
current_location = start_location

while the length of route does not equal list_of_stops:

    for every stop in list_of_stops:
    
        if stop is not in list_of_visited_stops:
        
            if stop distance from current_location is less than shortest_trip_distance:
                shortest_trip_distance = stop distance from current_location
                shortest_destination = stop
                
    append shortest_destination to route
    current_location = shortest_destination
    shortest_trip_distance = large number
    
```
### Programming Environment

#### The environment I used to develop this application:
    Operating System: macOS Big Sur
    IDE: Pycharm 
    Python Version: Python 3.8.3

### Space-time complexity of each major segment of the program

#### dispatch.py

| Methods               | Space-time complexity | 
| --------------------- |:---------------------:| 
| determine_next_stop() | O(n)                  |
| create_route()        | O(n<sup>2</sup>)      |
| create_list_of_stops()| O(n)                  |

#### fulfillment.py

| Methods                    | Space-time complexity | 
| -------------------------- |:---------------------:| 
| gather_packages_for_load() | O(n)                  |

#### util.py

| Methods                   | Space-time complexity | 
| ------------------------- |:---------------------:| 
| calculate_time()          | O(1)                  |
| gather_packages_for_load()| O(n)                  |
| convert_time()            | O(1)                  |

#### hash_table.py

| Methods                   | Space-time complexity | 
| ------------------------- |:---------------------:| 
| insert()                  | O(1)                  |
| search()                  | O(1)                  |
| remove()                  | O(1)                  |

#### csv_reader.py

| Methods                             | Space-time complexity | 
| ----------------------------------- |:---------------------:| 
| convert_address_to_id()             | O(n)                  |
| convert_address_id_to_address()     | O(1)                  |
| address_registry_cvs_to_hashtable() | O(n)                  |
| convert_cvs_to_hashtable()          | O(n)                  | 
| distance_csv_to_hashtable()         | O(n)                  |
| distance_lookup()                   | O(1)                  |

### Capability and Scalability

This application is not scalable. The time complexity of the algorithm used in the WGUPS Package Routing
algorithm is O(n<sup>2</sup>), so as the number of packages increases the time it takes to route the additional packages
will exponentially increase making this not a suitable solution to scale with. In the real world, this application would not be usable. In the real world, this application would have to work with restrictions that are outside of the scope that was imposed by the project requirement.

### Code Maintenance

This codebase is easy to maintain because the code is very readable which allows another developer to be able to understand what is happening. The code is also well documented which will help a person understand a
part of code.

### Strengths and Weaknesses of hashtable

The datatype used stored packages and addresses objects was a hashtable. This application reads through CSV files
that describes packages and addresses and inserts them into a hashtable.

#### Strengths
The main benefit of a hashtable is that it is usually  O(1) to look up or insert an element in it. This made inserting and retrieving package and address objects fast and efficient. If the number of trucks, or the number of cites
increase, the time it takes to look up a package would still be constant.

#### Weaknesses of Hashtable
A loss in performance can happen in a large hashtable because the hashtable suffers from bad cache performance.
This means it may take longer to retrieve an item, making the runtime O(n) (worst case).

### Alternative DataStructure

##### Linked List
A linked List could have been used to store data. The benefit of a linked list is that you can add or remove elements
from the beginning of the list at constant time, but when it comes to looking up a certain element is when you lose a
lot of performance. Compared to the hashtable that we used in this solution that takes constant time to lookup an element,
a linked list takes O(n) to lookup an element because you have to iterate through it to find an element.

#### Binary Tree
A binary search tree could have been used to store data for this program also. A binary search tree is a rooted binary
tree with internal elements each store a key greater than all the keys in the elements left subtree and less than those in
its right subtree. This would be an alternative to the hashtable because the time it takes to insert and search for an
element is O(log n). It's not O(1) like a hashtable but is still efficient.

### Alternative Algorithms


#### Farthest Insertion 

In the farthest insertion algorithms, you start with an arbitrary stop, in our case the hub, and find the farthest stop from that starting stop. Then you find the farthest stop from any of the previously found stops. Repeat the processes until all stops in the route are selected. This has a time complexity of O(n<sup>2</sup>).

#### Brute-Force Approach

This algorithm finds all possible routes for the truck to travel and chooses the one with the shortest distance. It does create an optimal solution, but as the number of stops in a route increase, the time to find all possible
routes can increase. The time complexity is O(n!)


### What would I do differently
One thing I would do differently if I attempted this project again would be to create code that would short the packages
into loads instead of manually sorting packages. I would still implement the nearest neighbors algorithm in this project.
