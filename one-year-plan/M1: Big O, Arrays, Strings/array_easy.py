# Q1, LC 896
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone
# decreasing if for all i <= j, nums[i] >= nums[j].
# Return true if and only if the given array nums is monotonic.


def find_mono(nums):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        return (True)
    else:
        return (False)


nums = [1, 2, 2, 2, 5, 6, 3]
print(find_mono(nums))


# Q2. LC 697
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency
# of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as num.
def find_degrees(nums):
    C = {}
    for i, n in enumerate(nums):
        if n in C:
            C[n].append(i)
        else:
            C[n] = [i]
    M = max([len(i) for i in C.values()])
    min_degree = float('inf')
    for i in C.values():
        if len(i) == M:
            degree = (i[-1] - i[0]) + 1
            min_degree = min(degree, min_degree)
    return min_degree

# Q3. LC 1480
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

def find_run_total(nums):
    run_total = [0] * len(nums)
    run_total[0] = nums[0]

    for i in range(1, len(run_total)):
        run_total[i] = nums[i] + run_total[i - 1]
    return run_total

    # for i in range(1, len(nums)):
    # 	nums[i] = nums[i] + nums[i-1]
    # return nums


# Q4. LC 349 Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
# must be unique and you may return the result in any order.
def find_intersect(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    intersect = []
    for i in nums1:
        if i in nums2:
            intersect.append(i)
    return intersect

# Q5. LC Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# Example:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


def find_2n(arr, n):
    final_arr = []
    for i in range(int(len(arr)/n)+1):
        final_arr.append(arr[i])
        final_arr.append(arr[i+n])
    return final_arr


# Q6. LC 1486. XOR Operation in an Array
# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

def xor_operation(start, n):
    ans = 0
    nums = [start + i * 2 for i in range(n)]

    for n in nums:
        ans = ans ^ n
    return ans


# Q7. 1408. String Matching in an Array
# Given an array of string words. Return all strings in words which is substring of another word in any order.
#
# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right
# side of words[j].
def find_substring(words):
    arr = ' '.join(words)
    subStr = [i for i in words if arr.count(i) > 1]
    return subStr

