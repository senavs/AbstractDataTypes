from .exceptions import Full, Empty
from .cell import Cell

class Queue:

	def __init__(self, data=[], max_size=0):
		self._max_size = max_size
		self._size = 0
		self._first_element = None
		self._last_element = None

		for data_item in data:
			self.enqueue(data_item)

	def empty(self):
		return self.size == 0

	def full(self):
		if self.max_size == 0:
			return False
		else:
			return self.size == self.max_size

	def peek(self):
		return self._first_element

	def find(self, data):
		if data == self._first_element.value:
			return self._first_element.value
		elif data == self._last_element.value:
			return self._last_element.value
		else:
			current_cell = self._first_element.next
			while current_cell.value != data:
				if not current_cell.next:
					return None
				current_cell = current_cell.next
			return current_cell.value

	def enqueue(self, data):
		if self.full():
			raise Full("Queue is already full.")
		
		new_cell = Cell(data)
		if self.size == 0:
			self._first_element = new_cell
			self._last_element = new_cell
		else:
			self._last_element.next = new_cell
			self._last_element = new_cell
		self._size += 1

	def dequeue(self):
		if self.empty():
			raise Empty('Queue is already empty')

		removed_cell = self._first_element.value
		if self.size == 1:
			self._first_element = None
			self._last_element = None
		else:
			self._first_element = self._first_element.next
		self._size -= 1
		return removed_cell

	@property
	def max_size(self):
		return self._max_size
	
	@property
	def size(self):
		return self._size
	
	def __str__(self):
		return ''

	def __repr__(self):
		return ''
