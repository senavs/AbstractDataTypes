# LinkedList

<p align="center">
  <img src="https://miro.medium.com/max/1200/1*iMYmkYDCSrXXdwpbqm-ekA.jpeg" width=500>
</p>


## What is that?

## What is that?

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
