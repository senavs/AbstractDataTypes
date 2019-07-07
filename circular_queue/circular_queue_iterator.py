from .utils import next_position, prev_position


class CircularQueueIterator:

	def __init__(self, circular_queue):
		self._circular_queue = circular_queue
		self._beginning = circular_queue._beginning
		self._end = circular_queue._end
		self._current = circular_queue._beginning
		self._first = True

	def __iter__(self):
		return self

	def __next__(self):
		if self._circular_queue.empty():
			raise StopIteration()

		if self._first:
			self._first = False
			return self._circular_queue._linear_data[self._current]
		else:
			self._current = next_position(self._current, self._circular_queue.max_size)
			if self._current == self._beginning:
				raise StopIteration()
			elif self._circular_queue._linear_data[self._current] is None:
				raise StopIteration()
			else:
				return self._circular_queue._linear_data[self._current]
