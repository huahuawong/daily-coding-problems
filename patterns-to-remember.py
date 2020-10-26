# List of important patterns to remember when you go to coding interviews:

# 1. Sliding window

# Common problems you use the sliding window pattern with:

# Maximum sum subarray of size ‘K’ (easy)
# Longest substring with ‘K’ distinct characters (medium)
# String anagrams (hard)


# So, let's say for instance, Given an array of integers of size ‘n’, we want to calculate the maximum sum of 
# ‘k’ consecutive elements in the array.

def findmax(arr, n, k):
  sum = 0
#first, we have to create a window of sum for the first one
  for i in range (k):
    window_sum = sum(arr[i])
  
  for i in range(n-k):
    window_sum = window_sum - arr[i] + arr[i+k]    #each window would minus the first one and add the next one
    maxsum = max(sum, window_sum)
    
  return maxsum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
k = 4
n = len(arr) 
print(maxSum(arr, n, k)) 

# 2. Two pointers or iterators, typically useful to search for pairs or a value in a sorted array or linked list
# When to use 2 pointers? when you're dealing with sorted array or linkedlist and you have to find a pair that fulfills certain criteria
# For instance, Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

import numpy as np

def findTriplets(arr, n):
    arr.sort()
    triplet_array = []
    for i in range(0, n - 1):
      l = i + 1
      r = n - 1
      x = arr[i]
      while (l < r):
        if (x + arr[l] + arr[r] == 0):
          triplet_array.append(np.array([x, arr[l],arr[r]]))
          l += 1
          r -= 1

        elif (x + arr[l] + arr[r] < 0):
          l += 1
        else:
          r -= 1
    return triplet_array

# Driven source
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)

# 3. Fast and Slow pointers
# The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move 
# through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays
# Cyclic arrays = a data structure that used a array as if it were connected end-to-end


