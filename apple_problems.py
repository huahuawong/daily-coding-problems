# This problem was asked by Apple.

# Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

# Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

# For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

# | 1 | 2 | 3 | 4 | 5 | 6 |
# | 2 | 4 | 6 | 8 | 10 | 12 |
# | 3 | 6 | 9 | 12 | 15 | 18 |
# | 4 | 8 | 12 | 16 | 20 | 24 |
# | 5 | 10 | 15 | 20 | 25 | 30 |
# | 6 | 12 | 18 | 24 | 30 | 36 |

# And there are 4 12's in the table.
# Basicallly the idea is to initialize an empty 2d array, and then create the multiplication table. Final step, is to check how many times the target number
# appear within the 2d array

def find_instances(size, target):
    arr = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            arr[i][j] = (i + 1) * (j + 1)

    count = 0
    for i in range(size):
        for j in range(size):
            if arr[i][j] == target:
                count += 1
    return count

print(find_instances(6, 12))

# ######################################################################################################################################################################
# This problem was asked by Apple.
#
# Given two sorted arrays of positive integers, and an integer k, determine the k smallest pairs among the two arrays,
# where a pair is defined as having exactly one element from the first array and one element from the second array.
#
# For example, if the k = 3 and the two arrays are [1, 3, 6, 10] and [2, 5, 7, 9] then [[1, 2], [3, 2], [1, 5]] since
# those are the three smallest pairs.


arr1 = [1, 3, 6, 10]; arr2 = [2, 5, 7, 9]
k = 3

import numpy as np


def find_smallest_k_pair(arr1, arr2, k):
    pairs_list = list()
    k_smallest_list = list()
    for num1 in arr1[0:int(np.ceil(k/2))]:
        for num2 in arr2[0:int(np.ceil(k/2))]:
            pairs_list.append([[num1, num2], num1+num2])
    pairs_list.sort(key=lambda i: i[1])
    k_smallest = pairs_list[0: k]
    for entry in k_smallest:
        k_smallest_list.append(entry[0])
    return k_smallest_list

print(find_smallest_k_pair(arr1, arr2, k))

# Alternate solution
n1 = len(arr1); n2 = len(arr2)
index2 = [0 for i in range(n1)]

while k > 0:
    # Initialize current pair sum as infinite
    min_sum = sys.maxsize
    min_index = 0

    # To pick next pair, traverse for all elements of arr1[], for every element, find corresponding
    # current element in arr2[] and pick minimum of all formed pairs.
    for i1 in range(0, n1, 1):
        # Check if current element of arr1[] plus element of array2 to be used gives minimum sum
        if index2[i1] < n2 and arr1[i1] + arr2[index2[i1]] < min_sum:
            # Update index that gives minimum
            a= arr1[i1]
            b = arr2[index2[i1]]
            min_index = i1
            # update minimum sum
            min_sum = arr1[i1] + arr2[index2[i1]]

    print("(", arr1[min_index], ",", arr2[index2[min_index]], ")", end=" ")

    index2[min_index] += 1

    k -= 1




