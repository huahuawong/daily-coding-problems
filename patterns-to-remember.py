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


# Another question is Squaring a sorted array (easy)
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def squareArray(nums, n):
    sq_arr = []
    left = 0; right = n - 1
    
    while left <= right:
        if abs(nums[left]) <= abs(nums[right]):
            sq_arr.append(nums[right]**2)
            right -= 1
        else:
            sq_arr.append(nums[left]**2)
            left += 1            
    return sq_arr[::-1]

nums = [-7,-3,2,3,11]
# nums = [-4,-1,0,3,10]
n = len(nums)
print(squareArray(nums, n))




# 3. Fast and Slow pointers
# The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move 
# through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays
# Cyclic arrays = a data structure that used a array as if it were connected end-to-end

# Example, let's say given a linked list, we want to see if there is a cycle within the linked list
def findcycle(head):
    head = hare = tortoise
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        
        if hare == tortoise:
            return True
            
    return False
  
# Another example is linkedlist palindrome
# Easiest way is if we use a list and simply check if it's the same when reversed, but this is not efficient
# Alternatively, we can use slow and fast pointer. The idea is to use 2 pointers to reach the midpoint and then traverse in a reversed order manner
def palindromeLinkedList(head):
  fast = slow = head 
  # This condition will allow the traversal to stop at midpoint
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    
  prev = None; next = None
  while slow:
    next = slow.next
    slow.next = prev
    prev = slow
    slow = next
    
  # Now we know that prev is at right end. And where's the left end? The head
  left, right = head, prev
  
  while right:
    if left.val != right.val:
      return False
    else:
      left = left.next; right = right.next
      
  return True

    
# 4. Merge Intervals
# The Merge Intervals pattern is an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals,
# you either need to find overlapping intervals or merge intervals if they overlap.

# Example: Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.

# To approach this problem, we need to understand when do intersections happen?
# Let's look at the sequence: A = [[0,2],[5,10]] and B = [[1,5],[8,12]], for the first element of the list, we can tell there is an overlap when A.end > B.start 
# and A.start < B.end, with that in mind, let's get to it

def findInterval(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
  res = []
  # initialize starting index to iterate through the array
  i = j = 0
  while i < len(A) and j < len(B):
    if A[i][0] <= B[j][-1] and B[j][0] <= A[i][-1]:
      res.append([max(A[i][0], B[j][0]), min(A[i][-1], B[j][-1])])    
    # if the end value of A is greater than B, we know we have to move on to the next A
    if A[i][-1] < B[j][-1]:
      i += 1
    else:
      j += 1
   return res

# 5. Inplace traversal of linkedlist
# Sometimes we may come across questions to reverse the linkedlist and without using extra memory, one way to do it is to use current, previous and next head node.
# Best reference with visualization: https://www.geeksforgeeks.org/reverse-a-linked-list/

def reverse(self):
    prev = None
    curr = self.head

    while curr != None:
        next_elem = curr.next
        curr.next = prev
        prev = curr
        curr = next_elem
    self.head = prev

# Tree BFS
# The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove 
# the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.
