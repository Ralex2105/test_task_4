class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Creates or retrieves an instance of the class.

        :param cls: The class being instantiated.
        :param *args: Variable length argument list for the class constructor.
        :param **kwargs: Keyword arguments for the class constructor.
        :return object: The single instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]