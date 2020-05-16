class SingletonMetaClass(type):
    """
    SingletonMetaClass is for implementing singleton, pass in to the class by using metaclass=SingletonMetaClass
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
