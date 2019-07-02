class DoublyLinkedListIterator:

	def __init__(self, beginning):
		self._current_cell = beginning
		self._firts = True

	def __iter__(self):
		return self

	def __next__(self):
		if self._firts:
			self._firts = False
		else:
			try:
				self._current_cell = self._current_cell.next
				getattr(self._current_cell, "value")
			except AttributeError:
				raise StopIteration()
		return self._current_cell.value
