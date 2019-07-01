from .cell import Cell
from .exceptions import *


class LinkedList:

	def __init__(self, max_size=0):
		self._beginning = None
		self._end = None
		self._size = 0
		self._max_size = max_size

	def empty(self):
        return self.size == 0

    def full(self):
        if self.max_size == 0:
            return False
        else:
            return self.size == self.max_size

    def insert(self, data, pos):
    	pass

    def append(self, data):
    	pass

    def pop(self, pos=self.size-1):
    	pass

    def replace(self, data, pos):
    	pass

    @property
    def size(self):
    	return self._size
    
    @property
    def max_size(self):
    	return self._max_size
    
