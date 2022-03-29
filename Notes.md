## What is an algorithm?

An algorithm is a set of instructions for accomplishing a task. Every piece of code can be called an algorithm.

## Binary Search

Searching for a name in a phone book or when Facebook tries to verify your username, it searches through its directory of authorised usenames. This is a *search problem*. 

This problem is solved using the *binary search* algorithm. It takes a **sorted list** of elements as its input. If the element you are looking for is in that list, the algorithm returns the position of the element. Otherwise, it returns `null`. 

Binary search carries out the following steps:

- Take the center element of the ordered list
- If the center element is too high, discard the upper half of the list. Else discard the lower half of the list.
- Repeat the process again in the remaining half till the correct element is found

With binary search, you eliminate half the elements every time. Thus, for any list of *n* elements, binary search takes **log<sub>2</sub>n** steps to run in the worst case, whereas simple search will take *n* steps.

The code for binary search can be found [here](binary_search.py).