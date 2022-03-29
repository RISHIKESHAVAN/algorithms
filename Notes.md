## What is an algorithm?

An algorithm is a set of instructions for accomplishing a task. Every piece of code can be called an algorithm.

## Running time of algorithms

If the maximum number of guesses is the same as the size of the list, then it is called *linear time*.

The *Big O* notation tells how fast an algorithm is. It’s not enough to just know how long an algorithm takes to run. You need to know how the running time increases as the list size increases. That’s where Big O notation comes in. 

For example, suppose you have a list of size n. Simple search needs to check each element, so it will take n operations. The run time in Big O notation is *O(n)*. Where are the seconds? There are none!! Big O doesn’t tell you the speed in seconds. Big O notation lets you compare the number of operations. It tells you how fast the algorithm grows. 

Also, Big O establishes a *worst-case* run time. Along with the *worst-case* run time, it’s also important to look at the *average-case* run time. 

The following are some common Big O run times, sorted from fastest to slowest:

- O(log n), known as *log time*. Example: Binary search
- O(n), known as *linear time*. Example: Simple search
- O(n * log n) Example: A fast sorting algorithm like *quicksort*
- O(n<sup>2</sup>) Example: A slow sorting algorithm like *selection sort*
- O(n!) Example: A *really* slow algorithm like *traveling salesperson*

**BEWARE: Algorithm running times grow at different rates.**

## Binary Search

Searching for a name in a phone book or when Facebook tries to verify your username, it searches through its directory of authorised usenames. This is a *search problem*. 

This problem is solved using the *binary search* algorithm. It takes a **sorted list** of elements as its input. If the element you are looking for is in that list, the algorithm returns the position of the element. Otherwise, it returns `null`. 

Binary search carries out the following steps:

- Take the center element of the ordered list
- If the center element is too high, discard the upper half of the list. Else discard the lower half of the list.
- Repeat the process again in the remaining half till the correct element is found

With binary search, you eliminate half the elements every time. Thus, for any list of *n* elements, binary search takes **log<sub>2</sub>n** steps to run in the worst case, whereas simple search will take *n* steps. Binary search runs in *logarithmic time*.

The code for binary search can be found [here](binary_search.py).