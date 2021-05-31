## What is array?
An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value.

### Advantages of using arrays: 
1. Arrays allow random access to elements. This makes accessing elements by position faster.
2. Arrays have better cache locality that can make a pretty big difference in performance.
3. Arrays represent multiple data items of the same type using a single name.

### How does array differ to tuple, or list?
Main difference between array and tuple is that array is mutable, i.e. you can modify it, but tuple is immutable.

Main difference between array and list is that array is of the same type of elements meaning all ints, or floats, but in a list, you can have different types. 
More info refer to [link](https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/)
 

### Array Syntax
1. To append something to the array, use `append()`
2. Removing element from array, use `pop()`, if you want to remove the third element, use `pop(2)`
3. Count number of elements with a specific value, use `count()`
4. Add elements to the array, use `extend()`. What is the difference between append and extend then? Append adds an object, whereas extend, kind of expands the list.
- Refer to this link for more info: https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
5. Returns index of the first element with the specified value, `index()`
6. Reverse the array, `reverse()`. Maybe useful for questions like determine if it's palindrone.
7. Sorting the array, `sort()`. Very useful with sorting problems such as binary search to find 2 integers that sum to a specific value.
