from .cell import Cell
from .exceptions import *


class DoublyLinkedList:

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
            raise Full("DoublyLinkedList is full")

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
            current_cell = self.search(pos, return_cell_class=True)
            new_cell.previous = current_cell.previous
            current_cell.previous.next = new_cell
            new_cell.next = current_cell
            current_cell.previous = new_cell

        self._size += 1

    def append(self, data):
        self.insert(data, self.size)

    def remove(self, pos):
        if self.empty():
            raise Empty("DoublyLinkedList is empty")

        if self.size == 1 and pos == 0:
            current_cell = self._beginning.value
            self._beginning = None
            self._end = None
        elif pos == 0:
            current_cell = self._beginning.value
            self._beginning.next.previous = None
            self._beginning = self._beginning.next
        elif pos == self.size - 1:
            current_cell = self._end.value
            self._end.previous.next = None
            self._end = self._end.previous
        else:
            current_cell = self.search(pos, return_cell_class=True)
            current_cell.previous.next = current_cell.next
            current_cell.next.previous = current_cell.previous
            current_cell = current_cell.value

        self._size -= 1
        return current_cell

    def replace(self, data, pos):
        current_cell = self.search(pos, return_cell_class=True)
        current_cell.value = data
        return True

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
    
    def __len__(self):
        return self.size
