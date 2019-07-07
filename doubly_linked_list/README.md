# DoublyLinkedList

<p align="center">
  <img src="https://miro.medium.com/max/1200/1*iMYmkYDCSrXXdwpbqm-ekA.jpeg" width=500>
</p>


## What is that?
&nbsp; A Doubly Linked List is the same as the [Linked List](https://github.com/senavs/AbstractDataTypes/edit/master/linked_list) when the subject is **implementation**, but, one attribute can make this abstract data type more efficient.  
&nbsp; Now, the list has an attribute point to the last element, which facilitates the **insert** and **reversed** methods.

## What is that?
&nbsp; The uses of a Doubly Linked List are the same as the [Linked List](https://github.com/senavs/AbstractDataTypes/edit/master/linked_list), but more efficient. 

## Complexity
| Algorithm | Average | Worst case |
| -- | -- | -- |
| Memory Space | O(*n*) | O(*n*) |
| Search | O(*n*) | O(*n*) |
| Insert | O(*n*) | O(*n*) |
| Insert Index 0 | O(1) | O(1) |
| Append | O(1) | O(1) |
| Remove | O(*n*) | O(*n*) |
| Reverse | O(*n*) | O(*n*) |

## How to use?
**Import**
``` python
from AbstractDataTypes import DoublyLinkedList
```

**New Queue instance**  
&nbsp; *max_size* specific the how many elements Queue can have. *DoublyLinkedList(max_size=0)* or *DoublyLinkedList()* create a ilimited doublylinkedlist.  
&nbsp; You can also initialize DoublyLinkedList with values, just passing an **__ iter __** object.  
``` python
dll = DoublyLinkedList()
print(dll)
# []
dll = DoublyLinkedList(range(10))
print(dll)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Append method**
&nbsp; Add an element at the end of the DoublyLinkedList.  
``` python
dll.append(10)
print(dll)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Insert method**
&nbsp; Add an element by the index.  
``` python
dll.insert(11, 5)
print(dll)
# [0, 1, 2, 3, 4, 11, 5, 6, 7, 8, 9, 10]
```

**Remove method**
&nbsp; Remove an element by the index.  
``` python
removed_1 = dll.remove(11)
print(removed_1)
# 10

removed_2 = dll.remove(0)
print(removed_2)
# 0

print(dll)
# [1, 2, 3, 4, 11, 5, 6, 7, 8, 9]
```

**Search method**
&nbsp; Search an element by the index.  
``` python
print(dll.search(4))
# 11
```

**Reverse**
  - **Reversed print**
  ``` python
  print(dll.rprint())
  # [9, 8, 7, 6, 5, 11, 4, 3, 2, 1]
  ```
  
  - **Reversed list**
  ``` python
  reversed_dll = reversed(dll)
  print(dll)
  # [9, 8, 7, 6, 5, 11, 4, 3, 2, 1]
  print(reversed_dll)
  # [9, 8, 7, 6, 5, 11, 4, 3, 2, 1]
  ```
