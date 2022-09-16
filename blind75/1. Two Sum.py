# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_arr = []
        for i in range(0, len(nums)-1):
            diff = target - nums[i]
            temp_arr = nums[:i] + nums[i + 1:]
            if diff in temp_arr:
                if nums.count(diff) == 2:
                    values_indexes = [i for i, j in enumerate(nums) if j == diff]
                    return values_indexes
                else:
                    index_arr.append(i)
                    index_arr.append(nums.index(diff))
                    return index_arr


# A more elegant way is to use the dictionary                  
class Solution(object):
    def twoSum(self, nums, target):
        buff = dict()
        for i in range(len(nums)):
            second_addend = target - nums[i]
            if second_addend in buff:
                return [buff[second_addend],i]
            else:
                buff[nums[i]] = i
