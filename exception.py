class StreamNameAlreadyExistsException(Exception):
    """Raised when attempting to create a stream which topic name already exists"""

    def __init__(self, name: str):
        super(StreamNameAlreadyExistsException, self) \
            .__init__(f'A stream with name \'{name}\' already exists!')


class SingletonInstanceAlreadyExistsException(Exception):
    """Raised when attempting to create a second instance of a singleton"""

    def __init__(self, type_: str):
        super(SingletonInstanceAlreadyExistsException, self) \
            .__init__(f'Tried to allocate a second instance of a singleton \'{type_}\'. Use getInstance() instead.')