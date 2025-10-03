#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    It implements a simple caching mechanism
    without any limit on item count or eviction policy.
    """
    def put(self, key, item):
        """
        Add an item to the cache.
        If either key or item is None, the method does nothing.
        Args:
            key: The key under which to store the item.
            item: The item to be stored.
        """
        if key is None or item is None:
            return
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
