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


# Q4
# You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

#     L, meaning the domino has just been pushed to the left,
#     R, meaning the domino has just been pushed to the right, or
#     ., meaning the domino is standing still.

# Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, 
# it will remain upright. For example, given the string .L.R....L, you should return LL.RRRLLL.
# Basically, the idea is to use 2 array appraoch. First, we initialize an array of zeroes of length n. or the first array, we iterate through the string and determine
# the right positions. If val = "R", then rDist variable = 0, if it's L, then nothing changes, else if rDist is not None, which means R was present prior to that, then
# we'd increment rDist and mark the rDist value at the dist.

# Similar thing is done for the left array, except we are iterating from the right to the left. If there is "L", then set lDist = 0, the difference is that right now,
# if lDist is not None, then we have to see if lDist < dist[i] or the current point is a ".", then we assign "L". If lDist == dist[i], that means it was moving "R", and
# that means, they'll be canceled out, thus it will be in "." state

def pushDominoes(dominoes):
    """
    :type dominoes: str
    :rtype: str
    """
    lst = list(dominoes)
    dist = [0] * len(dominoes)
    rDist = None
    for i, val in enumerate(lst):
        if val == 'R':
            rDist = 0
        elif val == 'L':
            rDist = None
        elif rDist != None:
            rDist += 1
            dist[i] = rDist
            lst[i] = 'R'
    lDist = None
    for i in range(len(lst) - 1, -1, -1):
        if dominoes[i] == 'L':
            lDist = 0
        elif dominoes[i] == 'R':
            lDist = None
        elif lDist != None:
            lDist += 1
            if lDist < dist[i] or lst[i] == '.':
                lst[i] = 'L'
            elif lDist == dist[i]:
                lst[i] = '.'
    return ''.join(lst)



# Q5 This problem was asked by Microsoft.
# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
# the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

seq = [2, 1, 5, 7, 2, 0, 5]

curr_seq = []

for num in seq:
    curr_seq.append(num)
    # Even length
    if len(curr_seq) % 2 == 0:
        curr_seq = sorted(curr_seq)
        print((curr_seq[int(len(curr_seq)/2)] + curr_seq[int(len(curr_seq)/2) - 1])/ 2)
    else:
        curr_seq = sorted(curr_seq)
        print(curr_seq[int(len(curr_seq)/2)])
        
        
# Q6. Implement a URL shortener with the following methods:
#
# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such shortened string exists,
# return null.

import random

URL_Dict = dict()
alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
alnum = list(alphabets+alphabets.upper()+numbers)


url = "https://www.google.com/"
short = "1405Dx"    # shortened url from random choice of alnum


def shorten(long_url):
    for shortURL in URL_Dict.keys():
        if URL_Dict[shortURL] == long_url:
            return f"This URL has already been shortened and stored, the shorted URL is {shortURL}"
    short_url = ""
    while len(short_url) < 6:
        short_url += random.choice(alnum)
    URL_Dict[short_url] = long_url
    if short_url in URL_Dict.keys():
        return ""
    return short_url


def restore(short_url):
    for short in URL_Dict.keys():
        if short == short_url:
            return URL_Dict[short]
    return "No such shortened URL exist"


print(shorten(url))
print(restore("1405Dx"))

# Q6. The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, 
# where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.



