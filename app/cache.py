import time


class Cache:
    """
    A simple cache implementation with time-to-live (TTL) functionality.
    """

    def __init__(self, ttl, not_found_obj=None):
        """
        Initializes the Cache object with a specified TTL and an optional not found object.

        Args:
            ttl (int): The time-to-live (TTL) in seconds for each cache entry.
            not_found_obj (optional): The value to return if a key is not found or has expired.
                Defaults to None.
        """
        self.ttl = ttl
        self.cache = {}
        self.not_found_obj = not_found_obj

    def set(self, key, value):
        """
        Stores a value in the cache with the specified key.

        Args:
            key: The key under which the value will be stored.
            value: The value to be stored in the cache.
        """
        self.cache[key] = {'value': value, 'time': time.time()}

    def get(self, key):
        """
        Retrieves a value from the cache by its key.

        Args:
            key: The key whose value needs to be retrieved from the cache.

        Returns:
            The value associated with the key if it exists and is valid; otherwise,
            returns `not_found_obj`.
        """
        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry['time'] < self.ttl:
                return entry['value']
            else:
                del self.cache[key]
        return self.not_found_obj
