class LinkedListIterator:

	def __init__(self, beginning):
		self._current_cell = beginning
		self._first = True

	def __iter__(self):
		return self

	def __next__(self):
		try:
			getattr(self._current_cell, "value")
		except AttributeError:
			raise StopIteration()
		else:
			if self._first:
				self._first = False
				return self._current_cell

			self._current_cell  = self._current_cell.next
			if self._current_cell is None:
				raise StopIteration()
			else:
				return self._current_cell.value
