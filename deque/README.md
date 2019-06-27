# Deque

<p align="center">
  <img src="http://www.java2novice.com/images/dequeue.png" width=500>
</p>

## What is that?
&nbsp;  Deque is a [Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) upgrade, which elements can be **added** to or **removed** from Deque.**head** or Deque.**tail**. 
Deque differs from the queue abstract data type (**FIFO**), because **[Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) can only add and remove elements using one side**.
In the other hand, **Deque has method that allows placed a new element at the begging or at the end** of the struct.

## Where to use it?
&nbsp;  In any situation. You can replace the [Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) to Deque just using its methods that substitutes *Queue.enqueue()* and *Queue.dequeue()*. 
It's only possible because Deque can add an element at the end and revome from the other (or vice versa).

## Complexity
| Algorithm | Average | Worst case |
| -- | -- | -- |
| Memory Space | O(*n*) | O(*n*) |
| Search | -- | -- |
| Insert | O(1) | O(1) |
| Delete | O(1) | O(1) |

## How to implement it?
&nbsp;  You can implement a Deque data type using the same classes in the [Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) data type. You just have to add the "enqueue" and "dequeue"
methods at the other side of the list.

## How to use AbstractDataTypes.deque.Deque?
**Import**  
``` python
from AbstractDataTypes import Deque
```
**New Deque instance**  
&nbsp; *max_size* specific the how many elements Deque can have. *Deque(max_size=0)* or *Deque()* create a ilimited deque.  
``` python
dq = Deque()
# <>
```
**Add elements by the head**
``` python
for c in range(10):
    dq.add_head(c)
# <9, 8, 7, 6, 5, 4, 3, 2, 1, 0>
```
**Add elements by the tail**
``` python
for c in range(10):
    dq.add_tail(c)
# <9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9>
```
**Remove**
&nbsp; The remove method return the removed item. You can also remove from head or tail
``` python
## Remove from head
dq.remove_head()
# 9
dq.remove_head()
# 8

## Remove from tail
dq.remove_tail()
# 9
``` 

