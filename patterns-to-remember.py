List of important patterns to remember when you go to coding interviews:

1. Sliding window

Common problems you use the sliding window pattern with:

Maximum sum subarray of size ‘K’ (easy)
Longest substring with ‘K’ distinct characters (medium)
String anagrams (hard)


So, let's say for instance, Given an array of integers of size ‘n’, we want to calculate the maximum sum of 
‘k’ consecutive elements in the array.

def findmax(arr, n, k):
  sum = 0
#first, we have to create a window of sum for the first one
  for i in range (k):
    window_sum = sum(arr[i])
  
  for i in range(n-k):
    window_sum = window_sum - arr[i] + arr[i+k]    #each window would minus the first one and add the next one
    maxsum = max(sum, window_sum)
    
  return maxsum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
k = 4
n = len(arr) 
print(maxSum(arr, n, k)) 

