import threading

from exception import SingletonInstanceAlreadyExistsException


class SingletonMixin:
    __lock = threading.Lock()
    __instance = None

    def __init__(self, *args, **kwargs):
        if self.__class__.__instance:
            raise SingletonInstanceAlreadyExistsException(type(self.__class__.__instance))

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = cls(*args, **kwargs)
        return cls.__instance