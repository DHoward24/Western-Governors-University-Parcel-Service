# HashTable class using chaining.
class ChainingHashTable:
    """
    A class to represent a person.

    Attributes
    ----------
    initial_capacity : int
        the initial size of the hashtable

    Methods
    -------
    insert:
        Inserts elements into the hashtable

    search:
        Search for elements in the hashtable

    remove:
        removes elements form the hashtable
    """

    def __init__(self, initial_capacity=40):
        """
        Constructs all the necessary attributes for the person object.
        Has a runtime of O(n).

        Parameters
        ----------
            initial_capacity : int
                The initial size of the hashtable
        """

        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        """
        Inserts elements into the hashtable.
        The runtime is O(1).

        Parameters
        ----------
            key : int
                Is the value used to lookup the element in the future

            item : Object
                The element that will be in the hashtable

        Returns
        -------
            True : boolean
                If the element was successfully inserted it return True
        """
        # does both insert and update
        # get the bucket list where this item will fo
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        """
        Constructs all the necessary attributes for the person object.
        Has a runtime of O(1).

        Parameters
        ----------
            key : int
                The value to look up an elements.

        Returns
        -------
            item : Object
                Object associated with key entered
        """
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            if key_value[0] == key:
                item = key_value[1]
                return item

            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        """
        Removes items from the hashtable.
        Runtime is O(1).

        Parameters
        ----------
        key : int
            The key of the item that needs to be removed.
        """
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)



