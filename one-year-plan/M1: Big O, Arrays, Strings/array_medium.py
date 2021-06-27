# Q1 LC 624. Maximum Distance in Arrays
# You are given m arrays, where each array is sorted in ascending order.
#
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define
# the distance between two integers a and b to be their absolute difference |a - b|.
# Return the maximum distance.

# Example: Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the
# second array.

arrays = [[1,2,3],[4,5],[1,2,3]]
def find_maxdiff(arrays):
    minnum = arrays[0][0]
    maxnum = arrays[0][-1]
    maxdiff = float('-inf')

    for array in arrays[1:]:
        maxdiff = max(maxdiff, array[-1] - minnum, maxnum - array[0])
        minnum = min(minnum, array[0])
        maxnum = max(maxnum, array[-1])

    return maxdiff


print(find_maxdiff(arrays))


# Q2. This problem was asked by Uber.
#
# Given a list of positive integers, return the maximum increasing subsequence, that is, the largest increasing
# subsequence within the array that has the maximum sum. Examples: if the input is [5, 4, 3, 2, 1] then return 5
# (since no subsequence is increasing), if the input is [3, 2, 5, 7, 6] return 15 = 3 + 5 + 7, etc.

import numpy as np

nums = [5, 4, 3, 2, 1]


def find_inc_subsequence(nums):
    curr_max = 0
    arr = []

    for i in range(0, len(nums)):
        if curr_max < nums[i]:
            curr_max = nums[i]
            arr.append(nums[i])
    return np.sum(arr)


# Q3. Given an array nums of n integers and an integer target, find three integers in nums such that the sum is
# closest to target. Return the sum of the three integers. You may assume that each input would have exactly
# one solution.

nums = [-1,2,1,-4]; target = 1
# expected output: 2  since (-1 + 2 + 1 = 2)

from itertools import permutations
import numpy as np

p = permutations(nums, 3)
min = float('inf')

# Brute force: Generate all permutations and evalute the set which would be the closest to target, However this solution
# may result in time limit exceeded
# Print the obtained permutations
for combo in list(p):
    # print(combo)
    cur_sum = np.sum(combo)
    if abs(cur_sum - target) < abs(min - target):
        min = cur_sum


# Second solution, using sort and 2 pointer system
nums.sort()
min = float('inf')

for i in range(len(nums)):
    j, k = i + 1, len(nums) - 1
    while j <k:
        cur_sum = nums[i] + nums[j] + nums[k]
        # if cur_sum == target:
        #     return cur_sum
        if abs(cur_sum - target) < abs(min - target):
            min = cur_sum
        if cur_sum > target:
            k -= 1
        else:
            j += 1


