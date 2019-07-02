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
        if self.full():
            raise Full("LinkedList is full")

        new_cell = Cell(data)
        if self.empty() and pos == 0:
            self._beginning = new_cell
            self._end = new_cell
        elif pos == 0:
            self._beginning.previous = new_cell
            new_cell.next = self._beginning
            self._beginning = new_cell
        elif pos == self.size:
            self._end.next = new_cell
            new_cell.previous = self._end
            self._end = new_cell
        else:
            current_cell = self.search(pos, True)
            new_cell.previous = current_cell.previous
            current_cell.previous.next = new_cell
            new_cell.next = current_cell
            current_cell.previous = new_cell

        self._size += 1

    def append(self, data):
        self.insert(data, self.size)

    def remove(self, pos):
        pass

    def replace(self, data, pos):
        pass

    def search(self, pos, return_cell_class=False):
        if pos >= self.size or pos < 0:
            raise IndexError(f"{pos} out of the range")

        returned_cell = self._beginning
        for index in range(self.size):
            if index == pos:
                break
            returned_cell = returned_cell.next

        if return_cell_class:
            return returned_cell
        return returned_cell.value            

    @property
    def size(self):
        return self._size
    
    @property
    def max_size(self):
        return self._max_size
    
