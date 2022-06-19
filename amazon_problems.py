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


############################################################################################################################
# Q8 Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or
# less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount
# of words. If there's no way to break the text up, then return null.
#
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each
# word. For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
# ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

from collections import defaultdict

string = "the quick brown fox jumps over the lazy dog"
k = 10
words = string.split()

def check_curr_len(dict, index):
    dict_values = dict[index]
    if len(dict_values) == 0:
        return 0
    length = 0
    for i in dict_values:
        length += len(i)
    length += len(dict_values) - 1     # account for space
    return length


def get_list_strings(test):
    mydict = defaultdict(list)
    index = 0; num_key = 0
    for i in range(len(test)):
        if check_curr_len(mydict, index) + len(test[i]) < k:
            # lst.append([test[i]])
            if num_key != len(mydict):
                mydict[index] = [test[i]]
                num_key += 1
            else:
                mydict[index].append(test[i])
                if check_curr_len(mydict, index) + len(test[i]) > k:
                    index += 1
    return mydict.items()


words_split = get_list_strings(words)



############################################################################################################################
# Q9 Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time


# This problem was asked by Amazon.

# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# For example, given the following matrix:

mat = [[1,  2,  3,  4,  5, 55],
       [6,  7,  8,  9,  10, 66],
       [11, 12, 13, 14, 15, 77],
       [16, 17, 18, 19, 20, 88],
       [111, 122, 133, 144, 155, 166]]


height = len(mat)
length = len(mat[0])

cur_height_s = 0; cur_height_m = height
cur_length_s = 0; cur_length_m = length

counter = 0

while counter != height * length:
    for i in range(cur_length_s, cur_length_m - 1):
        print(mat[cur_length_s][i])
        counter += 1

    for j in range(cur_height_s, cur_height_m - 1):
        print(mat[j][cur_height_m])
        counter += 1

    for i in range(cur_length_m - 1, cur_length_s, -1):
        print(mat[cur_height_m - 1][i])
        counter += 1

    cur_height_s += 1; cur_height_m -= 1
    for j in range(cur_height_m, cur_height_s -1, -1):
        print(mat[j][cur_length_s])
        counter += 1

    cur_length_s += 1; cur_length_m -= 1


arr = [1, 2, 3, 10]


# This problem was asked by Amazon.
# Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

# For example, for the input [1, 2, 3, 10], you should return 7.
# The idea is that we keep a candidate as 1, and we have to figure out what is the smallest positive integer that
# cannot be made using the fist k elements of the array

# THe plan is to scan from left to right, if at any point, the candidate is smaller than a value of the array, stop and
# return the candidate, else we just keep updating the candidate by adding it with the value from the array


def find_smallest_subset_sum(arr):
    candidate = 1
    for i in range(0, len(arr)):
        if arr[i] > candidate:
            return candidate
        else:
            candidate += arr[i]
    return candidate


assert(find_smallest_subset_sum(arr) == 7)
assert(find_smallest_subset_sum([1, 3, 6, 10, 11, 15]) == 2)
assert(find_smallest_subset_sum([1, 1, 1, 1]) == 5)
assert(find_smallest_subset_sum([1, 2, 5, 10, 20, 40]) == 4)
assert(find_smallest_subset_sum([1, 2, 3, 4, 5, 6]) == 22)

# This problem was asked by Amazon.

# An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# This is the easiest way, but this might be O(n)?
arr.index(num)

# The idea is:
# 1. Set a midpoint of the array
# 2. Check if arr[0......mid] is sorted, if it is:
# 	a. Check if num lies within the range of arr[0...mid], if it is then seach again for arr[0...mid-1]
# 	b. If not, repeat for arr[mid + 1 to end of array]
# 3. Repeat this for when the second part of the array is sorted


def search(arr, low, high, num):
    mid = (low + high) // 2
    
    if arr[mid] == num:
        return mid
    
    # How to check if arr[0], .... arr[mid] is sorted? check if first element is less than the mid element
    if arr[low] < arr[mid]:
        # If so, we can search within this range of elements recursively
        if num >= arr[low] and num <= arr[mid]:
            return search(arr, low, mid-1, num)
        return search(arr, mid + 1, high, num)
    
    # arr[mid...len(n)] should be sorted then
    if num >= arr[mid] and num <= arr[high]:
        return search(arr, mid + 1, high,  num)
    return search(arr, low, mid-1, num)

search(arr, 0, len(arr), 18)
