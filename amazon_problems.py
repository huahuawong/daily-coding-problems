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
def get_longest_sub_with_k_dist(s, k):
    if not s:
        return ""
    elif len(s) <= k:
        return s
    elif k == 1:
        return s[0]

    distinct_char_count = 0
    seen_chars = set()
    candidate = None
    remaining_string = None

    # to keep track of where the second character occurred
    first_char = s[0]
    second_char_index = 0
    while s[second_char_index] == first_char:
        second_char_index += 1

    candidate = s
    for index, char in enumerate(s):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char_count += 1

        if distinct_char_count > k:
            candidate = s[:index]
            remaining_string = s[second_char_index:]
            break
            
    longest_remaining = get_longest_sub_with_k_dist(remaining_string, k)
    
    longest_substring = None
    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring



