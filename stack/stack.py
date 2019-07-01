from .cell import Cell
from .exceptions import *


class Stack:

    def __init__(self, data=[], max_size=0):
        self._top = None
        self._size = 0
        self._max_size = max_size

        for data_item in data:
            self.push(data_item)

    def empty(self):
        return self.size == 0

    def full(self):
        if self.max_size == 0:
            return False
        else:
            return self.size == self.max_size

    def peek(self):
        return self._top

    def push(self, data):
        if self.full():
            raise Full("Stack is full")

        new_cell = Cell(data)
        if self.size == 0:
            self._top = new_cell
        else:
            new_cell.bellow = self._top
            self._top = new_cell
        self._size += 1

    def pop(self):
        if self.empty():
            raise Empty("Stack is empty")

        poped_cell = self._top.value
        if self.size == 1:
            self._top = None
        else:
            self._top = self._top.bellow
        self._size -= 1
        return poped_cell

    @property
    def size(self):
        return self._size
    
    @property
    def max_size(self):
        return self._max_size
    
    def _print_stack(self):
        if self.size == 0:
            return '<|'
        stack_string_print = '<'
        current_cell = self._top
        while current_cell.bellow is not None:
            stack_string_print += '%s, ' % current_cell.value
            current_cell = current_cell.bellow
        stack_string_print += '%s' % current_cell.value
        stack_string_print += '|'
        return stack_string_print

    def __repr__(self):
        return self._print_stack()
