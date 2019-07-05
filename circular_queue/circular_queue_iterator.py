from .utils import next_position, prev_position


class CircularQueueIterator:

	def __init__(self, circular_queue):
		self._queue = circular_queue
		self._data = circular_queue._linear_data		
		self._beginning = circular_queue._beginning
		self._end = circular_queue._end
		
		self._current_index = circular_queue._beginning
		self._first = True

	def __iter__(self):
		return self

	def __next__(self):
		if self._queue.empty():
			raise StopIteration()

		if self._first:
			self._first = False
		elif self._current_index != self._end:
			self._current_index = next_position(self._current_index, self._end)
			if self._current_index == self._beginning:
				raise StopIteration()
			elif self._data[self._current_index] is None:
				raise StopIteration()

		return self._data[self._current_index]
