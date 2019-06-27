from .exceptions import Full, Empty
from .cell import Cell


class Deque:

    def __init__(self, max_size=0):
        self._max_size = max_size
        self._size = 0
        self._head = None
        self._tail = None

    def empty(self):
        return self.size == 0

    def full(self):
        if self.max_size == 0:
            return False
        else:
            return self.size == self.max_size

    def _add(self, data, position):
        if self.full():
            raise Full("Deque is full.")

        new_cell = Cell(data)
        if self.size == 0:
            self._head = new_cell
            self._tail = new_cell
        elif position == 'head':
            self._head.left = new_cell
            new_cell.right = self._head
            self._head = new_cell
        else:
            self._tail.right = new_cell
            new_cell.left = self._tail
            self._tail = new_cell
        self._size += 1

    def add_head(self, data):
        self._add(data, 'head')

    def add_tail(self, data):
        self._add(data, 'tail')

    def _remove(self, position):
        if self.empty():
            raise Empty("Deque is empty.")

    def remove_head(self):
        pass

    def remove_rail(self):
        pass

    @property
    def max_size(self):
        return self._max_size
    
    @property
    def size(self):
        return self._size

    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail
