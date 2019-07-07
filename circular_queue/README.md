# Circular Queue

<p align="center">
  <img src="https://cdncontribute.geeksforgeeks.org/wp-content/uploads/Circular-queue.png" width=250>
</p>

## Whait is that?
&nbsp; Circular Queue is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end. This structure lends itself easily to buffering data streams.

## Modulo operation as method and attributes
- **Next Position:** (position + 1) % max_size
- **Previous Position:** (position - 1 + max_size) % max_size
- **If is empty:** beginning == end
- **If is full:** (end + 1) % max_size == beginning **or** next_position(end) % max_size

## How to use it?
**Import**
``` python
from AbstractDataTypes import CircularQueue
``` 

**Create an instance**
&nbsp; *max_size* specific the how many elements CircularQueue can have.  
&nbsp; You can also initialize CircularQueue with values, just passing an **__ iter __** object.  
``` python
cq = CircularQueue(max_size=10)
print(cq)
# <<

cq = CircularQueue(max_size=10, data=range(9))
print(cq)
# <0, 1, 2, 3, 4, 5, 6, 7, 8<
``` 
&nbsp; **OBS**: Beacuse of the modulo operation, your circular queue will be **max_size - 1 spaces to store** your data. Otherwise, It'll raise an **Full** Exception.
``` python
cq = CircularQueue(max_size=10, data=range(10))

Traceback (most recent call last):
  File: "C:\Users\root\Desktop\circular_queue.py
  cq = CircularQueue(max_size=10, data=range(10))
Full: Circular Queue is full
``` 

**Dequeue**
``` python
dequeued_item = cq.dequeue()
print(dequeued_item)
# 0
print(cq)
# <1, 2, 3, 4, 5, 6, 7, 8<
``` 

**Enqueue**
``` python
cq.enqueue(10)
print(cq)
# <1, 2, 3, 4, 5, 6, 7, 8, 10<
``` 

**Peek**
``` python
print(cq.peek())
# 1
```
