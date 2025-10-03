#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching.
    It implements the MRU (Most Recently Used) caching strategy:
    when the cache exceeds the maximum number of items,
    the most recently used item is discarded.
    """
    def __init__(self):
        """
        Initialize the cache.
        Calls the parent constructor and
        initializes a list to track usage order.
        """
        super().__init__()
        self.key_save = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds the max size,
        discard the most recently used item (MRU).
        If the key already exists,
        update its position to the end (most recently used).
        Args:
            key: The key under which to store the item.
            item: The item to be stored.
        """
        if key is None or item is None:
            return
        if key in self.key_save:
            self.key_save.remove(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_key = self.key_save.pop()
            del self.cache_data[most_key]
            print(f"DISCARD: {most_key}")
        self.key_save.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by its key.
        Updates the usage order to mark the key as most recently used.
        Args:
            key: The key of the item to retrieve.
        Returns:
            The item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.key_save.remove(key)
        self.key_save.append(key)
        return self.cache_data.get(key)
