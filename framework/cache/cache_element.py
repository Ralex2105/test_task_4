import logging


class CacheElement:
    def __init__(self):
        """
        Initializes a new instance of the CacheElement class.
        """
        logging.debug("Initialized CacheElement.")
        self._element_cache = {}

    def get_cached_element(self, name, find_element_func):
        """
        Retrieves a cached element by name, or finds and caches it if not present.
        :param name: The name of the element to retrieve from the cache.
        :param find_element_func: A function that returns the element.
        :returns WebElement: The cached element with the specified name.
        """
        if name not in self._element_cache:
            logging.debug(f"Element '{name}' not found in cache.")
            self._element_cache[name] = find_element_func()
            logging.debug(f"Element '{name}' find and put cache.")
        else:
            logging.debug(f"Element '{name}' in cache.")
        return self._element_cache[name]

    def reset_element_cache(self, name=None):
        """
        Resets the cached elements.

        :param name: The name of the element to remove from the cache.
        :param name = None: the entire cache is cleared.
        """
        if name:
            if name in self._element_cache:
                del self._element_cache[name]
                logging.debug(f"Element '{name}' removed from cache.")
            else:
                logging.warning(f"'{name}' was not found to remove from cache.")
        else:
            self._element_cache.clear()
            logging.debug("Cache is reset")
