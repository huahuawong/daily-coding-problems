# Q1
# You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. 
# Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

def find_min_jump(arr, n):
    jumps = [0 for i in range(n)]

    # Eliminate some base case
    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0

    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if i <= (arr[j] + j) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


# Driver Program to test above function
arr = [1, 3, 6, 1, 0, 9]
size = len(arr)
print('Minimum number of jumps to reach',
      'end is', find_min_jump(arr, size))
