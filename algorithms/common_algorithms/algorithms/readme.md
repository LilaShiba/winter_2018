# Algorithms

An algorithm is a process with unambiguous steps that has a beginning and an end, and does something useful.


Algorithmic thinking is taking a step back and asking, “If it’s the case that algorithms are so useful in computing to achieve predictability, might they also be useful in everyday life, when it comes to, say, deciding between alternative ways of solving a problem or completing a task?” In all cases, we optimize for efficiency: We care about time or space.

Note the mention of “deciding between.” Computer scientists do that all the time, and I was convinced that the tools they use to evaluate competing algorithms would be of interest to a broad audience.

- Ali Almossawi
[source](http://mitsloan.mit.edu/newsroom/articles/how-to-use-algorithms-to-solve-everyday-problems/)


### Algorithms We Will Cover

- Sequential search 
- Binary search 
- Bubble sort 
- Selection sort


## Sorting Algorithms

Sorting is ordering a list of objects. We can distinguish two types of sorting. If the number of objects is small enough to fits into the main memory, sorting is called internal sorting. If the number of objects is so large that some of them reside on external storage during the sort, it is called external sorting. 

All sorting algorithms share the goal of outputting a sorted list, but the way that each algorithm goes about this task can vary. When working with any kind of algorithm, it is important to know how fast it runs and in how much space it operates, in other words, its time complexity and space complexity

The running time describes how many operations an algorithm must carry out before it completes. The space complexity describes how much space must be allocated to run a particular algorithm. For example, if an algorithm takes in a list of size n , and for some reason makes a new list of size n for each element in n , the algorithm needs n** space.


#### Taken from:
- [source1](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html)

- [source2](https://brilliant.org/wiki/sorting-algorithms/)

#### TLDR  

An algorithm is a set of guidelines that describe how to perform a task. A sorting algorithm sorts a list. Each algorithm comes with cons and pros.

## Bubble Sort
We will walk through how to do a bubble sort in python, and then we will move to creating a recursive bubble sort.

#### Resources
- [See adt/stack/stack_walk.py for bubble sort in action](https://github.com/kyle1james/2017-2018_year_one_ibcs/blob/master/ADT/stack/stack_walk.py)

- [bubble sort video](http://zabana.me/notes/algorithms-in-python-bubble-sort.html)
- [bubble sort walk through](http://zabana.me/notes/algorithms-in-python-bubble-sort.html)
![bubble sort](https://codingcompiler.com/wp-content/uploads/2017/10/bubble-sort-in-c.png)

## Selection Sort
#### Source 1
The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.

#### Source 2
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray


#### Resources
- See adt/stack/stack_walk.py for selection sort in action
- See adt/queue/queue.py for selection sort in action

- [Source 1](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html)
[Video of Selection Sort](https://www.youtube.com/watch?v=mI3KgJy_d7Y)
- [Source 2](https://www.geeksforgeeks.org/selection-sort/)

## Searching Algorithms

A search algorithm is any algorithm which solves the search problem, namely, to retrieve information stored within some data structure



## Sequential search 
- [Source 1](https://www.geeksforgeeks.org/linear-search/)
A simple approach is to do linear search, i.e

- Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
- If x matches with an element, return the index.
- If x doesn’t match with any of elements, return -1.


Linear search is rarely used practically because other search algorithms such as the binary search algorithm and hash tables allow significantly faster searching comparison to Linear search.


![Sequential Search](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/Linear.png)

## Divide & Conquer


#### Binary Search: 
- [Source 2](https://www.geeksforgeeks.org/binary-search/)
Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

![Binary Search](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/binary-search1.png)


We basically ignore half of the elements just after one comparison.

- Compare x with the middle element.
- If x matches with middle element, we return the mid index.
- Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
- Else (x is smaller) recur for the left half.

[binary search](https://www.youtube.com/watch?v=IcK2Qyk3cUs)

## Big O
[source](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/)
Big O notation is used in Computer Science to describe the performance or complexity of an algorithm. Big O specifically describes the worst-case scenario, and can be used to describe the execution time required or the space used (e.g. in memory or on disk) by an algorithm

#### O(1)
O(1) describes an algorithm that will always execute in the same time (or space) regardless of the size of the input data set.

#### O(N)
O(N) describes an algorithm whose performance will grow linearly and in direct proportion to the size of the input data set. The example below also demonstrates how Big O favours the worst-case performance scenario; a matching string could be found during any iteration of the for loop and the function would return early, but Big O notation will always assume the upper limit where the algorithm will perform the maximum number of iterations.
