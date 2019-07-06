from ..deque.deque import Deque, Cell
from .exceptions import InconsistentMaxSize


class DequeuedQueue(Deque):

    def __init__(self, max_size):
        if max_size <= 0:
            raise InconsistentMaxSize("DequeuedQueue has max_size greater than 0")
        super().__init__(max_size)

    def _add(self, data, position):
        removed_cell = None
        if self.full():
            if position == 'head':
                removed_cell = self.remove_tail()
            else:
                removed_cell = self.remove_head()

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
        return removed_cell

    def add_head(self, data):
        return self._add(data, 'head')

    def add_tail(self, data):
        return self._add(data, 'tail')
