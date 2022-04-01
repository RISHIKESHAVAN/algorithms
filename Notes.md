# GROKKING ALGORITHMS

## What is an algorithm?

An algorithm is a set of instructions for accomplishing a task. Every piece of code can be called an algorithm.

## Running time of algorithms

If the maximum number of guesses is the same as the size of the list, then it is called *linear time*.

The *Big O* notation tells how fast an algorithm is. It’s not enough to just know how long an algorithm takes to run. You need to know how the running time increases as the list size increases. That’s where Big O notation comes in. 

For example, suppose you have a list of size n. Simple search needs to check each element, so it will take n operations. The run time in Big O notation is *O(n)*. Where are the seconds? There are none!! Big O doesn’t tell you the speed in seconds. Big O notation lets you compare the number of operations. It tells you how fast the algorithm grows. 

Also, Big O establishes a *worst-case* run time. Along with the *worst-case* run time, it’s also important to look at the *average-case* run time. 

The following are some common Big O run times, sorted from fastest to slowest:

- **O(log n)**, known as *log time*. Example: Binary search
- **O(n)**, known as *linear time*. Example: Simple search
- **O(n * log n)** Example: A fast sorting algorithm like *quicksort*
- **O(n<sup>2</sup>)** Example: A slow sorting algorithm like *selection sort*
- **O(n!)** Example: A *really* slow algorithm like *traveling salesperson*

[algo-runtime](images/algo-runtime.png)

**BEWARE: Algorithm running times grow at different rates.**

## Binary Search

Searching for a name in a phone book or when Facebook tries to verify your username, it searches through its directory of authorised usenames. This is a *search problem*. 

This problem is solved using the *binary search* algorithm. It takes a **sorted list** of elements as its input. If the element you are looking for is in that list, the algorithm returns the position of the element. Otherwise, it returns `null`. 

Binary search carries out the following steps:

- Take the center element of the ordered list
- If the center element is too high, discard the upper half of the list. Else discard the lower half of the list.
- Repeat the process again in the remaining half till the correct element is found

With binary search, you eliminate half the elements every time. Thus, for any list of *n* elements, binary search takes **log<sub>2</sub>n** steps to run in the worst case, whereas simple search will take *n* steps. Binary search runs in *logarithmic time*.

The code for binary search can be found [here](python-files/01_binary_search.py).

## Selection Sort

Lets say you want to sort a list of items in descending order. Selection sort works in the following way:
- Go through the array of items and get the biggest number. Place it first in a separate list.
- Now, go through the array of items again and find the current biggest number and append it to the separate list
- Repeat the process till all the elements are removed from the orginal list.

Time taken for selection sort to run: *O(n<sup>2</sup>)*. Although selection sort is a neat algorithm, it is not very fast.

Yes, the algorihm doesn’t have to check a list of n elements each time. You check n elements, then n – 1, n - 2 ... 2, 1. On average, you check a list that has 1/2 × n elements. The runtime is O(n × 1/2 × n). But constants like 1/2 are ignored in Big O notation, so you just write O(n × n) or O(n<sup>2</sup>).

The code for selection sort can be found [here](python-files/02_selection_sort.py).

## Recursion

Recursion is where a function calls itself. Example:

```
def look_for_key(box): 
  for item in box:
    if item.is_a_box(): 
      look_for_key(item)
    elif item.is_a_key(): 
      print “found the key!”
```

When you write a recursive function, you have to tell it when to stop recursing. That’s why every recursive function has two parts: 
- *recursive case* - when the function calls itself
- *base case* - when the function doesn’t call itself again; so it doesn’t go into an infinite loop!! 

## Stacks

Stacks are similar to arrays and lists but with a key difference that when you insert an item, it gets added to the top of the list and when you read an item, you only read the topmost item, and it’s taken off the list.
So, stacks have only 2 operations:
- *push* - adds a new item to the top
- *pop* - remove the top most item and read it

Your computer uses a stack internally called the *call stack*. This stack is used to save the call order and the variables for multiple functions. The top most function in the stack is the one that is currently being dealt with. All the other functions in the stack that are under the current function (these functions are basically the parent functions of the current function) are said to be *partially completed*. When you call a function from another function, the calling function is paused in a partially completed state. 

For each child function, the stack also keeps track of the list of unfinished items at that stage. Thus using stack is convenient. But it comes with a cost: saving all that info can take up a lot of memory. Each of those function calls takes up some memory, and when your stack is too tall, that means your computer is saving information for many function calls. At that point, you have two options:
- You can rewrite your code to use a loop instead.
- You can use something called *tail recursion* (advanced topic and is supported by only some languages)

