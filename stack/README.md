# Stack

## What is that?
&nbsp; Stack is an abstract data type that serves as a collection of elements.
To keep the order as a real stack, **LIFO** (**L**ast **I**n **F**irst **O**It) rule is followed. 
This abstract data type is implemented with three methods:
- **PUSH** - Insert elements at the top of the stack.
- **POP** - Remove elements at the top of the stack and return them.  
- **PEEK** - Return the element at the top of the list without *pop* it.  

## Where to use it?
&nbsp; One great exemple of Stack is in a [math expression compiler calculator](https://github.com/senavs/MathExpressionCompiler). [Queue](https://github.com/senavs/AbstractDataTypes/tree/master/queue) is also used in this process, but stack presence is essential.

## How to use?
** Import ** 
``` python
from AbstractDataTypes import Stack
```
** Create a Stack Instance ** 
&nbsp; *max_size* specific the how many elements Queue can have. *Stack(max_size=0)* or *Stack()* create a ilimited stack.  
&nbsp; You can also initialize Stack with values, just passing an **__ iter __** object.
``` python
s = Stack()
s = Stack([0, 2, 4, 6, 8])
# <8, 6, 4, 2, 0|
```
