# LinkedList

<p align="center">
  <img src="https://miro.medium.com/max/1200/1*iMYmkYDCSrXXdwpbqm-ekA.jpeg" width=500>
</p>


## What is that?
&nbsp; A linked list is a sequence data structure, which connects elements, called **Cell**s. Each Cells/Nodes are linked to the next element by pointers, but, the last element, is linked to None.  
&nbsp; The worst thing in LinkedList is the linear management. In other words, if you want to access the last element in the list, you'll have to pass through all the others elements, like the image above.

## Where to use it?
&nbsp; You can use a LinkedList as a Array, but if you'll need to access elements after the first element, I'll recoment a [DoublyLinkedList](https://github.com/senavs/AbstractDataTypes/edit/master/doubly_linked_list/). A LinkedList is efficient when is used as a [Queue](https://github.com/senavs/AbstractDataTypes/edit/master/queue/), which complexity will be O(1) for insert and remove element from the list.

## Complexity
| Algorithm | Average | Worst case |
| -- | -- | -- |
| Memory Space | O(*n*) | O(*n*) |
| Search | O(*n*) | O(*n*) |
| Insert | O(*n*) | O(*n*) |
| Append | O(1) | O(1) |
| Remove | O(*n*) | O(*n*) |

## How to use?
**Import**
``` python
from AbstractDataTypes import LinkedList
```

**New Queue instance**  
&nbsp; *max_size* specific the how many elements Queue can have. *LinkedList(max_size=0)* or *LinkedList()* create a ilimited linkedlist.  
&nbsp; You can also initialize LinkedList with values, just passing an **__ iter __** object.  
``` python
ll = LinkedList()
print(ll)
# []
ll = LinkedList(range(10))
print(ll)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Append method**
&nbsp; Add an element at the end of the LinkedList.  
``` python
ll.append(10)
print(ll)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Insert method**
&nbsp; Add an element by the index.  
``` python
ll.insert(11, 5)
print(ll)
# [0, 1, 2, 3, 4, 11, 5, 6, 7, 8, 9, 10]
```

**Remove method**
&nbsp; Remove an element by the index.  
``` python
removed_1 = ll.remove(11)
print(removed_1)
# 10

removed_2 = ll.remove(0)
print(removed_2)
# 0

print(ll)
# [1, 2, 3, 4, 11, 5, 6, 7, 8, 9]
```

**Search method**
&nbsp; Search an element by the index.  
``` python
print(ll.search(4))
# 11
```
