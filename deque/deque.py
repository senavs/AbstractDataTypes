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
        
        if self.size == 1:
            removed_cell = self._head.value
            self._head = None
            self._tail = None
        elif position == 'head':
            removed_cell = self._head.value
            self._head.right.left = None
            self._head = self._head.right
        else:
            removed_cell = self._tail.value
            self._tail.left.right = None
            self._tail = self._tail.left
        self._size -= 1
        return removed_cell

    def remove_head(self):
        return self._remove('head')

    def remove_tail(self):
        return self._remove('tail')

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

    def _print_deque(self):
        if self.size == 0:
            return '<>'
        deque_string_print = '<'
        current_cell = self._head
        while current_cell.right is not None:
            deque_string_print += '%s, ' % current_cell.value
            current_cell = current_cell.right
        deque_string_print += '%s' % current_cell.value
        deque_string_print += '>'
        return deque_string_print

    def __repr__(self):
        return self._print_deque()

    def __len__(self):
        return self.size
