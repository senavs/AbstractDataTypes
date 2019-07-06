# Binary Search Tree

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/200px-Binary_search_tree.svg.png" width=250>
</p>

## What is that?
&nbsp; A **binary search tree** is a data structure that stores "items" (such as numbers, names etc.) in memory. It allows fast lookup, addition and removal of items, and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by its key

## Complexity 
| Algorithm | Average | Worst case |
| -- | -- | -- |
| Memory Space | O(*n*) | O(*n*) |
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

## How to use it?
**Import**
``` python
from AbstractDataTypes import Tree
```

**Create an instance**
``` python
tree = Tree()
```

**Adding data to the Tree**
``` python
tree.add(12, 'item with key 12')
tree.add(5, 'item with key 5')
tree.add(15, 'item with key 15')
tree.add(3, 'item with key 3')
tree.add(7, 'item with key 7')
tree.add(13, 'item with key 13')
tree.add(17, 'item with key 17')
tree.add(1, 'item with key 1')
tree.add(9, 'item with key 9')
tree.add(19, 'item with key 19')
```
###### NOTE: You can also add data as a Tree parameter
``` python
data = {12: 'item with key 12', 5: 'item with key 5', 15: 'item with key 15',
        3: 'item with key 3', 7: 'item with key 7', 13: 'item with key 13',
        17: 'item with key 17', 1: 'item with key 1', 9: 'item with key 9',
        19: 'item with key 19'}

tree = Tree(data)
```

<p align="center">
  <img src="https://github.com/senavs/AbstractDataTypes/blob/master/binary_search_tree/images/tree_0.png" width=350>
</p>

**Remove**
``` python
tree.remove(5)
```

<p align="center">
  <img src="https://github.com/senavs/AbstractDataTypes/blob/master/binary_search_tree/images/tree_1.png" width=350>
</p>

``` python
tree.remove(19)
```

<p align="center">
  <img src="https://github.com/senavs/AbstractDataTypes/blob/master/binary_search_tree/images/tree_2.png" width=350>
</p>

``` python
tree.remove(3)
```

<p align="center">
  <img src="https://github.com/senavs/AbstractDataTypes/blob/master/binary_search_tree/images/tree_3.png" width=350>
</p>

``` python
tree.remove(12)
```

<p align="center">
  <img src="https://github.com/senavs/AbstractDataTypes/blob/master/binary_search_tree/images/tree_4.png" width=350>
</p>
