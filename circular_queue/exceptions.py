class CircularQueueException(Exception):
	pass

class Full(CircularQueueException):
	pass

class Empty(CircularQueueException):
	pass
