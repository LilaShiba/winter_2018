# Abstract Data Types

### Reading for this Unit
- http://web.mit.edu/6.005/www/fa14/classes/08-abstract-data-types/


Abstract data types are an instance of a general principle in software engineering, which goes by many names with slightly different shades of meaning. ADTs enable us to separate how we use a data structure in a program from the particular form of the data structure itself

- Talk about data’s behavior NOT its implementation:

- Behavior is defined by a set of values and a set of operations

## Why?
Abstraction provides a promise that any implementation of the ADT has certain properties and abilities; knowing these is all that is required to make use of an ADT object. 

The user does not need any technical knowledge of how the implementation works to use the ADT. In this way, the implementation may be complex but will be encapsulated in a simple interface when it is actually used

You can very well implement the ADT functionality using an array, but you are not sure as to the size of the array your app would require , so you end up using a stack/queue.

Stack/Queue are ideal for enforcing sequential rules of access (LIFO & FIFO as you stated) while Array is ideal for allowing random access as desired.

## Stack
A Stack is a particular type of linked list object where items are always added to the top, and always removed from the top of the list, so for this reason, the stack is called a last-in-first-out data structure (LIFO)

![stack](https://www.tutorialspoint.com/data_structures_algorithms/images/stack_representation.jpg)

## Queue
First-in-first-out data structure (FIFO)

A Queue is a particular type of linked list object (ADT) where items are always added to the front of the list, and always removed from the back of the list
![queue](http://www.cs.rmit.edu.au/online/blackboard/chapter/05/documents/contribute/chapter/04/images/queue.gif)

## Linked List
A linked list is a linear data structure where each element is a separate object. 
Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node, which is the pointer.

![linked list](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3HFm29zJxsS4mTUu2TjsH80noiZzc0CwX2kUOEJorRFcMoLXR)
## Binary Tree
Is a finite set of nodes which is either empty or consists of a data item (called the root) and two disjoint binary trees (called the left and right subtrees of the root), together with a number of access procedures
![Binary Tree](https://introcs.cs.princeton.edu/java/44st/images/binary-tree.png)

## Common Errors
- Seg Fault
A segmentation fault (aka segfault) is a common condition that causes programs to crash; they are often associated with a file named core . Segfaults are caused by a program trying to read or write an illegal memory location


