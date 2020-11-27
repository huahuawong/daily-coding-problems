# Q1 Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.

# For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.
MAXN = 105  # assume maximum value of n here

# dp[i] = number of max heaps for i distinct integers
dp = [0] * MAXN # intiialize dp arrays

# nck[i][j] = number of ways to choose j elements
#             from i elements, no order 
nck = [[0 for i in range(MAXN)] for j in range(MAXN)]

# log2[i] = floor of logarithm of base 2 of i, height of tree is always log2[i]
log2 = [0] * MAXN

# to calculate nCk， from n choose k elements
def choose(n, k):
    if (k > n):
        return 0
    if (n <= 1):
        return 1
    if (k == 0):
        return 1

    if (nck[n][k] != -1):
        return nck[n][k]

    answer = choose(n - 1, k - 1) + choose(n - 1, k)
    nck[n][k] = answer
    return answer


# calculate l for give value of n
def getLeft(n):
    if (n == 1):
        return 0

    h = log2[n]

    # max number of elements that can be present in the
    # hth level of any heap
    numh = (1 << h)  # (2 ^ h)

    # number of elements that are actually present in
    # last level(hth level)
    # (2^h - 1)
    last = n - ((numh) - 1)

    # if more than half-filled
    if (last >= (numh // 2)):
        return (1 << h) - 1  # (2^h) - 1
    else:
        return (1 << h) - 1 - ((numh // 2) - last)

    # find maximum number of heaps for n


def numberOfHeaps(n):
    if n <= 1:
        return 1

    left = getLeft(n)
    ans = (choose(n - 1, left) * numberOfHeaps(left)) * (numberOfHeaps(n - 1 - left))
    dp[n] = ans
    return ans


# function to initialize arrays
def solve(n):
    for i in range(n + 1):
        dp[i] = -1

    for i in range(n + 1):
        for j in range(n + 1):
            nck[i][j] = -1

    currLog2 = -1
    currPower2 = 1

    # for each power of two find logarithm
    for i in range(1, n + 1):
        if (currPower2 == i):
            currLog2 += 1
            currPower2 *= 2
        log2[i] = currLog2
    return numberOfHeaps(n)


# Driver code
n = 4
print(solve(n))


# Q2 Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified
# number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49

def get_two_sum(num, arr):
    i, k = 0, len(arr) - 1
    while i < k:
        a = arr[i]
        b = arr[k]
        target_sum = a + b
        if target_sum == num:
            return (a, b)
        elif target_sum < num:
            i += 1
        else:
            k -= 1


def find_subarraysum(arr, target):
    arr.sort()
    for i in range(len(arr)):
        matching = arr[i]
        if matching > target:
            continue
        twos = get_two_sum(target - matching, arr[:i] + arr[i+1:])
        if twos:
            return True
    return False


# Q3
# Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k

# The most straight forward way to do it is to use 3 loops and keep iterating through the numbers, if the sum is found, then return True, but this would result in O(n^3)
# The alternate way is to use 2 pointers, intiialize i from 0 to the array lenghth - 2, minus 2 in this case since we are considering 2 pointers, and the left pointer is i + 1
# We will also be using left and right pointer, left would be i+1, and right is the last element of the array
# Basically for i = 0, it'd be arr[0] + arr[1] + arr[5] (assuming it;s 5 element array), if the sum of these 3 is smaller than the target, then we increment i

def find3Numbers(A, arr_size, sum): 
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element one by one and find the other two elements  
    for i in range(0, arr_size-2): 
      
  
        # To find the other two elements, start two index variables from two corners of the array and 
        # move them toward each other 
          
        # index of the first element in the remaining elements 
        l = i + 1 
          
        # index of the last element 
        r = arr_size-1 
        while (l < r): 
          
            if( A[i] + A[l] + A[r] == sum): 
                print("Triplet is", A[i],  
                     ', ', A[l], ', ', A[r]); 
                return True
              
            elif (A[i] + A[l] + A[r] < sum): 
                l += 1
            else:
                r -= 1
  
    # If we reach here, then no triplet was found 
    return False
  
# Driver program to test above function  
A = [1, 4, 45, 6, 10, 8] 
sum = 22
arr_size = len(A) 
  
find3Numbers(A, arr_size, sum) 



arr = [20, 303, 4, 25]
k = 49
print(find_subarraysum(arr, k))






