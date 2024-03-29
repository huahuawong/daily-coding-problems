#1 Let's say if we want to move the zeroes in an array to the back of an array

def moveZerosToEnd(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

    return arr

# Drive code
arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0, 0, 8, 9, 7]
n = len(arr)
print(moveZerosToEnd(arr, n))


###########################################################################################################################################
#2 Situation is reversed, bring the zeroes to the front

def moveZerosToFront(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    for i in range(count, n-1):
        arr.pop()

    while count < n:
        var = 0
        arr.insert(0, var)
        count += 1

    return arr
    
# Driver code
arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0, 0, 8, 9, 7]
n = len(arr)
print(moveZerosToFront(arr, n))

###########################################################################################################################################

#3 Given an array, rotate the array to the right by k steps, where k is non-negative.

For example:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

input = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotate_input(arr):
    pop_arr = []
    for i in range(0, k):
        pop_var = arr.pop()
        pop_arr.insert(0, pop_var)

    output = pop_arr + arr

    return output


print(rotate_input(input))


Or even easier:

def rotate(nums, k):
      n = len(nums)
      k = k % n
      nums[:] = nums[n-k:] + nums[:n-k]

      return nums

###########################################################################################################################################


#4 Given a m x n matrix, if an element is 0, set its entire row and column to 0.


def setZeroes(self, matrix):
        isCol = False
        R = len(matrix)   #get length of row
        C = len(matrix[0])  #get length of column
        
        for i in range(R):
            if matrix[i][0] == 0:    #which means matrix[0][0] is 0, so isCol would be true, making all the values in column 0, zero
                isCol = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0    #if found zero, set the first element of the corresponding row and column to 0
                    matrix[i][0] = 0
        
        for i in range(1, R):           #continue updating the zeroes
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j]=0
                    
        if matrix[0][0] == 0:           #to make all the element in the first row zero
            for j in range(C):
                matrix[0][j] = 0
                
        if isCol:                       #to make all the element on the first column zero
            for i in range(R):
                matrix[i][0] = 0
        
        
#Driver code
matrix = [[0,1,2,0],[3,4,5,2], [1,3,1,5]]

###########################################################################################################################################

#5 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Easiest way to do it is searching the array one by one, Alternative way is binary search, which is harder. Let's do binary.

def Binarysearch(nums, target)

    if not nums:
        return -1

    low, high = 0, len(nums) - 1  #first, we get the high and low point
    
    while low <= high:
        middle = (low + high)/2       #and then we get the middle point
    
        if nums[mid] == target:
            return mid
    
        if nums[low] <= nums[mid]:    #recall that this is a sorted array, so if nums[mid] is larger than nums[low] means that target should be at 
            if nums[low] <= target <= nums[mid]:    #the left hand side
                high = mid - 1
            else:
                low = mid + 1
    return -1
    
    
###########################################################################################################################################
# 6 Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose 
sum equals to k.    

# basically what we need to do is to use a dictionary that contains the sum of integers from 0 to i
# d.get(sum - k, 0) gets key of 1 if the sum exists in the dict, if not returns a 0
def subarraySum(nums, k):
    count = 0
    sum = 0
    d = dict()
    d[0] = 1

    for num in nums:
        sum = sum + num
        count += d.get(sum-k, 0)    # returns 0 if no keys are found
        d[sum] = d.get(sum,0) + 1

    return count
    
    
nums = [1,1,1] 
k = 2

###########################################################################################################################################
# 7, Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
      
        nums1[m:] = nums2[:n]
        nums1.sort()
        
        return nums1

###########################################################################################################################################
# 8 This problem was asked by Apple.

# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements
# , return a fixed point, if one exists. Otherwise, return False

def findindex (arr):
    index = 0
    
    for num in arr:
        if num  == index:
            return num
        else:
            index += 1
            continue

    return False
    


arr = [-6, 0, 1, 40]
print(findindex(arr))

###########################################################################################################################################
# 9 An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat,
# and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

# For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number 
# of boats required will be three. 

# total = 0
import math

def calc_min(weights, k):
    total = 0
    for weight in weights:
        total += weight
        # print(total)
    min_num = math.ceil(total / k) 
    return min_num

weights = [100, 200, 150, 80]
total = 0
k = 200
print(calc_min(weights, k))
    
###########################################################################################################################################
# 10 Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger
# than 20,100.

# imports that can be used to permutate the strings
from itertools import permutations

def find_anagram(s, word):
    indices = []
    perms = [''.join(p) for p in permutations(word)]
    for i in range(0, len(s) - len(p) + 1):
        substring = s[i: i + len(p)]
        if substring in perms:
            indices.append(i)
    return indices

# Driver code to test
s = "cbaebabacd"
word = "abc"

# The idea is we generate permutations of the word and check if each substring in the array contains the word. It workds but
# it'd take a really long time to compute if we have this as input:
s = "aaaaaaaaaa"
word = "aaaaaaaaaaaaa"

# So alternatively,
from collections import Counter

def findAnagrams(s, p):
    indices_array = []
    l = len(p)
    counter_p = Counter(p)
    counter_s = Counter(s[:l - 1])
    i = 0
    while i + l <= len(s):
        counter_s[s[i + l - 1]] += 1
        if counter_s == counter_p:
            indices_array.append(i)
        counter_s[s[i]] -= 1
        if counter_s[s[i]] == 0:
            del counter_s[s[i]]
        i += 1
    return indices_array

print(find_anagram(s, word))

###########################################################################################################################################
# 11. Integer to Roman conversion
def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0 
        while num > 0:
            for iteration in range(num// val[i]):
                roman_num += syb[i]
                num += val[i]
            i -= 1
        return roman_num             

print(int_to_Roman(45))

