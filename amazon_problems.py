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
###
############################################################################################################################
# Q4 Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.
# k is guaranteed to be smaller than the length of the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    def get_element(self, target):
        temp = self.head
        count = 0
        while count < target:
            count += 1
            temp = temp.next
        return temp

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

llist = LinkedList(["a", "b", "c", "d", "e"])

k = 4
target_num = llist.getCount() - k
element = llist.get_element(target_num)
llist.remove_node(str(element))

############################################################################################################################
# Q5 Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

def spiralPrint(m, n, a): 
    k = 0
    l = 0
  
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
  
    while (k < m and l < n): 
  
        # Print the first row from the remaining rows 
        for i in range(l, n): 
            print(a[k][i], end=" ") 
  
        k += 1
  
        # Print the last column from the remaining columns 
        for i in range(k, m): 
            print(a[i][n - 1], end=" ") 
  
        n -= 1
  
        # Print the last row from the remaining rows 
        if (k < m): 
  
            for i in range(n - 1, (l - 1), -1): 
                print(a[m - 1][i], end=" ") 
  
            m -= 1
  
        # Print the first column from the remaining columns 
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                print(a[i][l], end=" ") 
  
            l += 1
  
  
# Driver Code 
a = [[1,  2,  3,  4,  5],
      [6,  7,  8,  9,  10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20]]
  
R = len(a)
C = len(a[0])
  
# Function Call 
spiralPrint(R, C, a) 

############################################################################################################################
# Q6 Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and 
# character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume 
# the string to be decoded is valid.
def encode(st, n):
	i = 0
	while i < n-1:
		count = 1
		while i < (n-1) and st[i] == st[i+1]:
			count += 1
			i += 1
		i += 1
		print(st[i - 1] + str(count), end = "")
		
		
string = "AAAABBBCCDAA"
n = len(string)
print(encode(string, n))

############################################################################################################################
# Q7 An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array). You can assume all the integers in the array are unique.
# Since we are trying to do better than linear time, we can do log(n), which is the time complexity of log(n)
# Question is how do we incorporate it, we know that the array is rotated, so we just need to find the picot point. First, we initialize the pivot as the middle, i.e.
# (len(arr) //2), using this pivot, let's see if the array from arr[0] to arr[mid] is sorted, if it is, great! We can try searching if the key is within this span
# of array, if it is, then we keep doing binary search from arr[low] to arr[mid -1], else we know that it has to be on the other half of the array, so we search from
# arr[mid+1] to arr[high]

# If arr[low] to arr[mid] was not sorted, then do the same thing but reversed. Why do we have to make sure it's sorted you asking? That is because binary search 
# works only on a sorted set of elements. To use binary search on a collection, the collection must first be sorted

def search(arr, low, high, key):
    mid = int((low + high)/2)
    if arr[mid] == key:
        return mid

    # If arr[low to mid] is sorted
    if arr[low] <= arr[mid]:
        if arr[low] <= key and arr[mid] >= key:
            return search(arr, low, mid -1, key)
        return search(arr, mid+1, high, key)

    if key >= arr[mid] and key <= arr[high]:
        return search(arr, mid+1, high, key)
    return search(arr, low, mid-1, key)


# Driver program
arr = [9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8]
key = 6
i = search(arr, 0, len(arr) - 1, key)
if i != -1:
    print("Index: % d" % i)
else:
    print("Key not found")
