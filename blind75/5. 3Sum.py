# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


# The solution is based on the concept of 2 pointers. The idea is to initialize a laft pointer that iterates from 0 to len(nums)-2, why?
# that is because you need at least 3 numbers for this problem, so the last case you'd have is left = nums[-3], mid = nums[-2], right = nums[-1]

# as for mid and right, we just need to increment and decrement based on the conditions

def threeSum(nums):
    res = []  # Initialize empty array
    nums.sort()  # Sort the array of nums

    for left in range(0, len(nums) - 2):
        # to check for duplicates, we use condition "left > 0" because we dont need to check when left == 0 (at the very beginning)
        if left > 0 and nums[left] == nums[left - 1]:
            continue
        mid = left + 1
        right = len(nums) - 1

        while mid < right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                mid += 1
            else:      # this means we found a combination that equals to 0
                res.append([nums[left], nums[mid], nums[right]])

                while mid < right and nums[mid] == nums[mid + 1]:
                    mid += 1
                while mid < right and nums[right] == nums[right - 1]:
                    right -= 1
                mid += 1;
                right -= 1
    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

