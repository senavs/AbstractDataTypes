class QueueException(Exception):
    pass

class Empty(QueueException):
    pass

class Full(QueueException):
    pass