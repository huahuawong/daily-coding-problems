# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def get_largest_non_adj(arr):
    # create 2 variables, previous and largest, initialize as 0
    prev, largest = 0, 0
    # iterate through the array, for each loop, keep track of the largest by finding max((previous + current value),
    # largest) and previous by assigning largest to it
    for curr_val in arr:
        prev, largest = largest, max(prev + curr_val, largest)
    return largest


print(get_largest_non_adj([3, 2, 6, 8, 10, 20]))
