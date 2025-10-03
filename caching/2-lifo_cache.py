#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.
    It implements the LIFO (Last-In, First-Out) caching strategy:
    when the cache exceeds the maximum number of items,
    the most recently added item is discarded.
    """
    def __init__(self):
        """
        Initialize the cache.
        Calls the parent constructor and
        initializes a list to track insertion order.
        """
        super().__init__()
        self.key_save = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds the max size,
        discard the most recently added item (LIFO).
        Args:
            key: The key under which to store the item.
            item: The item to be stored.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.key_save.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.key_save.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by its key.
        If the key is None or not found, return None.
        Args:
            key: The key of the item to retrieve.
        Returns:
            The item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
