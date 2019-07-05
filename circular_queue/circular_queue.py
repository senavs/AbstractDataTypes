from .utils import next_position, prev_position
from .exceptions import Full, Empty
from .circular_queue_iterator import CircularQueueIterator


class CircularQueue:

    def __init__(self, max_size, data=[]):
        self._linear_data = [None for _ in range(max_size)]
        self._beginning = 0
        self._end = 0 
        self._size = 0
        self._max_size = max_size

        for data_item in data:
            self.enqueue(data_item)

    def empty(self):
        return self._beginning == self._end

    def full(self):
        return next_position(self._end, self.max_size) == self._beginning

    def enqueue(self, data):
        if self.full():
            raise Full('Circular Queue is full')
        self._linear_data[self._end] = data
        self._end = next_position(self._end, self.max_size)
        self._size += 1

    def dequeue(self):
        if self.empty():
            raise Empty('Circular Queue is empty')
        dequeued_data = self._linear_data[self._beginning]
        self._linear_data[self._beginning] = None
        self._beginning = next_position(self._beginning, self.max_size)
        self._size -= 1
        return dequeued_data

    def peek(self):
        return self._linear_data[self._beginning]

    def print(self):
        if self.empty():
            return '<<'

        string = '<'
        for data in self:
            string += '%s, ' % data
        return string[:-2] + '<'

    @property
    def size(self):
        return self._size
    
    @property
    def max_size(self):
        return self._max_size

    def __iter__(self):
        return CircularQueueIterator(self)

    def __len__(self):
        return self._length

    def __repr__(self):
        return self.print()
