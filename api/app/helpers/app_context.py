from app.helpers import SingletonMetaClass
import logging
import flask


class AppContext(metaclass=SingletonMetaClass):
    """
    AppContext is the global context for logging, db etc..

    Args:
        metaclass ([type], optional):  Defaults to SingletonMetaClass.
    """

    def __init__(self):
        # set logger level
        self.logger = logging.getLogger('global_logger')
        self.logger.setLevel(logging.DEBUG)
        self.db = ""