from .cell import Cell
from .linked_list_iterator import LinkedListIterator


class LinkedList:

    def __init__(self, data=[], max_size=0):
        self._beginning = None
        self._size = 0
        self._max_size = max_size

        for data_item in data:
            self.append(data_item)
    
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
        elif pos == 0:
            new_cell.next = self._beginning
            self._beginning = new_cell
        else:
            current_cell = self.search(pos-1, True)
            new_cell.next = current_cell.next
            current_cell.next = new_cell

        self._size += 1

    def append(self, data):
        self.insert(data, self.size)

    def remove(self, pos):
        if self.empty():
            raise Empty("DoublyLinkedList is empty")
        if pos >= self.size or pos < 0:
            raise IndexError(f"{pos} out of the range")

        if self.size == 1 and pos == 0:
            current_cell = self._beginning.value
            self._beginning = None
        elif pos == 0:
            current_cell = self._beginning.value
            self._beginning = self._beginning.next
        else:
            search_cell = self.search(pos-1, True)
            current_cell = search_cell.next.value
            search_cell.next = search_cell.next.next

        self._size -= 1
        return current_cell

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

    def print(self):
        if self.size == 0:
            return '[]'
        string = '['
        for item in self:
            string += '%s, ' % item
        return string[:-2] + ']'

    @property
    def size(self):
        return self._size
    
    @property
    def max_size(self):
        return self._max_size

    def __len__(self):
        return self.size

    def __repr__(self):
        return self.print()

    def __iter__(self):
        return LinkedListIterator(self._beginning)
