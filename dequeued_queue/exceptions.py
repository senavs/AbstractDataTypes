from ..deque.exceptions import DequeException

class DequeuedQueue(DequeException):
	pass

class InconsistentMaxSize(DequeuedQueue):
	pass
