# Dequeued Queue

## What is that?
&nbsp; A Dequeued Queue is an extension of [Deque](https://github.com/senavs/AbstractDataTypes/tree/master/deque) but with a new feature.
Instead of raise an exception when the colloction is full, it'll remove and return the firts element in the other side.  
&nbsp; Eg: If the DequeuedQueue if <1, 2, 3, 4, 5> and you want to add the element 6 to the head (*add_head* method), this method will return the number 5 and add 6 to head. The collection will like that: <6, 1, 2, 3, 4>. The same occurs with *add_tail*, but it'll return the firts element of the Dequeued Queue and add to the tail.

## How to use it?
**Import**
``` python
from AbstractDataTypes.dequeued_queue.dequeued_queue import DequeuedQueue
```

**Create an instance**
###### NOTE: Dequeue Queue must have max_size greater than 0. Otherwise It will be a simple Deque.
``` python
dd = DequeuedQueue(10)
for i in range(10):
    dd.add_head(i)
print(dd)
# <9, 8, 7, 6, 5, 4, 3, 2, 1, 0>
```

**The feature only occurs when the Dequeued Queue is full**
``` python
print(dd.full())
# True
```

**Add Tail**
``` python
dequeued_item = dd.add_tail(-1)
print(dequeued_item)
print(dd)
# 9
# <8, 7, 6, 5, 4, 3, 2, 1, 0, -1>
``` 

**Add Head**
``` python
dequeued_item = dd.add_head(-1)
print(dequeued_item)
print(dd)
# -1
# <10, 8, 7, 6, 5, 4, 3, 2, 1, 0>
``` 
