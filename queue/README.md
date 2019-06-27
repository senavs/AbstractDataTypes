# Queue

<p align="center">
  <img src="https://cdn-images-1.medium.com/max/1200/1*wN83zdV3arHyUl5GQXxRfw.jpeg" width=500>
</p>

## What is that?
&nbsp; Queue is an abstract data type which keeps all data in order by following the rule **FIFO** (**F**ist **I**n, **F**ist, **O**ut).
This colletion data type has two principal methods. The firts one is **enqueue** or **add**, which places an new element in the end of 
the struct. The other one is called **dequeue**, **pop** or even **remove**, which takes out the first element and return it.

## Where to use it?
&nbsp; Queue is used in situations that the **order** cares and you won't need to access the data at the middle or at the end of the struct.
If you need get the elements at the same order you placed than, so Queue is a good colletion data type.

## Complexity
| Algorithm | Average | Worst case |
| -- | -- | -- |
| Memory Space | O(*n*) | O(*n*) |
| Search | O(*n*) | O(*n*) |
| Insert | O(1) | O(1) |
| Delete | O(1) | O(1) |

## How to implement it?
&nbsp; All data placed in the queue is first stored in a **Cell** class, which has **value** and **next** with attributes. When a new data is
placed, this data is now a Cell object and the **next** attribute of the last element added/placed now is pointing to this new Cell.  
&nbsp; The **Queue** class only points to the first and last Cell to favor the **queue** and **dequeue** methods.

## How to use AbstractDataTypes.queue.Queue?
**Import**  
``` python
from AbstractDataTypes import Queue
```
**New Queue instance**  
&nbsp; *max_size* specific the how many elements Queue can have. *Queue(max_size=0)* or *Queue()* create a ilimited queue.  
&nbsp; You can also initialize Queue with values, just passing an **__ iter __** object.
``` python
qu = Queue()
# < <

qu = Queue([0, 2, 4, 6, 8])
# <0, 2, 4, 6, 8<
```
**Enqueue**
``` python
qu.enqueue(10)
# <0, 2, 4, 6, 8, 10<
```
**Dequeue**
``` python
qu.dequeue()
# <2, 4, 6, 8, 10<
```
