#1 This question was asked by Google.

# You are given an array of length n + 1 whose elements belong to the set
# {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. 

# Find it in linear time and space.

# pigeonhole principle - states that if items are put into containers, with, then at least one container 
# must contain more than one item. 

# if we can modify the array
def detect_Dupli(nums):
       nums.sort()
       for i in range(1, len(nums)):
           if nums[i] == nums[i-1]:
               return nums[i]

# if it can't be modified

class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1


#2 You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
# For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

#   1
#  2 3
# 1 5 1

# The weight of the path is the sum of the entries, which would be 1+3+5 = 9 in this case


# First thing to do is to figure out the approach
# We can always start from the bottom row, and move up row by row
# but when we move up row by row, we should only check two adjacent elements on that row

def findmaxpath(nums):
       n = len(nums) - 1       # get the index of the last row, i.e. the bottom row
       memo = [None] * len(nums)
       
       for i in range(len(nums)):
           memo[i] = nums[n][i]
       
       for i in range(len(nums) - 2, -1, -1): # we minus two because we are looking at second to last row 
           for j in range(len(nums[i + 1]) - 1):
              memo[j] = nums[i][j] + max(nums[i], nums[i+1])
       return memo[0]       
       
#Driver code
A = [[2],
     [9, 3],
     [1, 6, 7],
     [2, 4, 5, 6],
     [3, 6, 9, 5, 2]]
     
     
#3 This problem was asked by Google. In linear algebra, a Toeplitz matrix is one in which the elements 
on any given diagonal from top left to bottom right are identical.
 
Write a program to determine whether a given input is a Toeplitz matrix. 
 
def isDiagonal(mat, i, j):
    res = mat[i][j]
    i += 1
    j += 1

    while i < len(mat) and j < len(mat[0]):

        # mismatch found
        if (mat[i][j] != res):
            return False

        i += 1
        j += 1

    # we only reach here when all elements
    # in given diagonal are same
    return True


def isToeplitz(mat):
    for j in range(len(mat[0])):
        if not isDiagonal(mat, 0, j):
            return False

    for i in range(len(mat)):
        if not isDiagonal(mat, i, 0):
            return False

    return True


mat = [[6, 7, 8, 9],
       [4, 5, 7, 8],
       [1, 4, 6, 7],
       [0, 1, 4, 6],
       [2, 0, 1, 4]]


M = len(mat[0])
N = len(mat)

if (isToeplitz(mat)):
    print("Matrix is a Toeplitz")
else:
    print("Matrix is not a Toeplitz")

 
# 4 You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance
# at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.
 
# the first intuition is to iterate from the beginning of the array, but the easier way is to iterate from the end, specifically from second to end array to the first item
# but of course we can consider the edge case, which is if the first element of the array is 0, the end can never be reached
# To iterate from end to the beginning, if the index has jump count which can reach to or beyond the last position, we'll update the last location to i

def find_path(arr, n):
      if arr[0] == 0:
             return False
        
      last_position = n -1
    
      for i in range(len(arr)-2,-1,-1): 
              if (i + arr[i]) >= last_position: 
                    last_position = i 
      return last_position == 0   
  
# arr = [1, 3, 1, 2, 0, 1]
arr = [0, 2, 1, 3, 0]
n = len(arr)
print(find_path(arr, n))
     
# 5 The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
# For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
# Given two strings, compute the edit distance between them.
def cal_editdistance(string_1, string_2):
    arr1 = []; arr2 = []
    edit_dist = 0
    for i in string_1:
        arr1.append(i)
        
    for j in string_2:
        arr2.append(j)

    for i in range(min(len(arr1), len(arr2))):
        if arr1[i] != arr2[i]:
            edit_dist += 1
    
    edit_dist = edit_dist + abs((len(arr2)-len(arr1)))
    return edit_dist
    

string_1 = "kitten"
string_2 = "sitting"

print(cal_editdistance(string_1, string_2))


# 6 This problem was asked by Google.
# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element 
# in the original input array.

def find_smallest(arr, n):
    count_arr = []
    i = 0
    while len(count_arr) != len(arr):
        cur_elem  = arr[i]
        j = i + 1
        count = 0
        while j < len(arr):
            if cur_elem > arr[j]:
                count += 1
                j += 1
            else: 
                j += 1
        count_arr.append(count)
        i += 1
    return count_arr
    

arr = [5, 7, 3, 8, 1]
print(find_smallest(arr, len(arr)))

# 7 This problem was asked by Google.
# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.


# 8. The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
import math

def powerset(set, set_size):
    # find the expected number of subsets, which would be 2^n, where n is the length of the set
    pow_set_size = (int)(math.pow(2, set_size))
       
    for counter in range(0, power_set_size):
       for j in range(0, set_size):
            # Check if jth element is a set, if it is a set, then print jth element from set
            if (counter & (1 << j)) > 0:
                print(set[j], end = "")
            print("")
    print("[]")

# Driver program to test printPowerSet
set = ['a', 'b', 'c']
printPowerSet(set, 3)

# 9. This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

# The keyword here is 'estimate', we are not calculating and are merely estimating
# Second thing, what is Monte Carlo method? It is also known as a multiple probability simulation, which means we generate a list of possible outcomes and based on them, we can get a numerical result

# Now, how do we bring Monte Carlo method to calculate area of a circle. We know that equation of circle is x^2 _ y^2 = r^2. Assuming that r = 1, we'd have x^2 + y^2 = 1. 
# Now what we have to do is to think generate a list of possible outcomes using what? x and y. And we can see if it falls inside the circle, by checking if x^2 + y^2 <= 1

# This link explained it well with diagrams for clarity: https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
import random

def estimate_pi(INTERVAL):
    circle_points = 0
    square_points = 0

    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(INTERVAL**2):
        # Randomly generated x and y values from a uniform distribution. Range of x and y values is -1 to 1
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        # Distance between (x, y) from the origin
        origin_dist= rand_x**2 + rand_y**2

        # Checking if (x, y) lies inside the circle
        if origin_dist<= 1:
            circle_points+=1
        square_points+=1

        # Estimating value of pi, pi= 4*(no. of points generated inside the
        # circle)/ (no. of points generated inside the square)
        pi = 4 * circle_points/ square_points
    return pi


# print(rand_x, rand_y, circle_points, square_points, "-", pi)
print("Final Estimation of Pi=", estimate_pi(5))


# 10. Given an array of elements, return the length of the longest subarray where all its elements are distinct.
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
def find_longest(num):
       return (len(set(num)))

arr = [5, 1, 3, 5, 2, 3, 4, 1]
print(find_longest(arr))
