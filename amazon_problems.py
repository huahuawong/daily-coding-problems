#1 Given a string, determine whether any permutation of it is a palindrome.

# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
# daily should return false, since there's no rearrangement that can form a palindrome.

NO_OF_CHARS = 256

def canformPalindrone(st):
    # Create a count array and initialize
    # all values as 0
    count = [0] * NO_OF_CHARS

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
    # a little confusing but basically we count the characteres to check
    # if there is more than one odd values, cause if there is, then palindrone can;t be formed

    # Count odd occurring characters
    odd = 0

    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            odd = odd + 1

        if (odd > 1):
            return False

    # Return true if odd count is 0 or 1,
    return True


str = "mmo"
print(canformPalindrone(str))


############################################################################################################################
#2 Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

def findSmallest(arr, n): 
  
    res = 1 #Initialize result, we start from 1 because it cant be represented if it's not in the array, and also smallest one
  
    # Traverse the array and increment 
    # 'res' if arr[i] is smaller than 
    # or equal to 'res'. 
    for i in range (0, n ): 
        if arr[i] <= res: 
            res = res + arr[i]   #the reason we increment by that is because if arr[i] is smaller or equals to res,
                                 #means that we can represent the numbers from 0 to i
        else: 
            break
    return res 
    
    
array = [1, 1, 3, 4] 
n1 = len(array) 
print(findSmallest(array, n1))

############################################################################################################################
#3 Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

# define character range
CHAR_RANGE = 128

# Function to find longest substring of given containing
# k distinct characters using sliding window
def longestSubstr(str, k):
    if not str:
        return ""
    elif len(str) <= k:
        return str
    elif k == 1:
        return str[0]
    
	# stores longest substring boundaries
	end = begin = 0

	# set to store distinct characters in a window
	window = set()

	# count list to store frequency of characters present in current window
	# we can also use a dictionary instead of count list
	freq = [0] * CHAR_RANGE

	# [low..high] maintain sliding window boundaries
	low = high = 0

	while high < len(str):

		window.add(str[high])
		freq[ord(str[high])] = freq[ord(str[high])] + 1

		# if window size is more than k, remove characters from the left
		while len(window) > k:

			# if the frequency of leftmost character becomes 0 after
			# removing it in the window, remove it from set as well
			freq[ord(str[low])] = freq[ord(str[low])] - 1
			if freq[ord(str[low])] == 0:
				window.remove(str[low])

			low = low + 1	   # reduce window size

		# update maximum window size if necessary
		if end - begin < high - low:
			end = high
			begin = low

		high = high + 1

	# return longest substring found at str[begin..end]
	return str[begin:end + 1]
