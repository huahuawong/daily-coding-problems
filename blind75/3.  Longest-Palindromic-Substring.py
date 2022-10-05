# https://leetcode.com/problems/longest-palindromic-substring/
  
# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"


# The following code works but it is not memory efficient, so let's try a second option
def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    max_len = n
    k = n

    if len(s) == 1:
        return s

    while n!= 1:
        if k == n:
            window = s[0:n]
            if window == window[::-1]:
                return window
            else:
                k -= 1
                continue

        for i in range(k):
            window = s[0:k]
            if window == window[::-1]:
                return window

        for i in range(max_len-k):
            window = window[1:] + s[k+i]
            if window == window[::-1]:
                return window
            else:
                continue
        k -= 1
        n -= 1

        
# Second approach, using dynamic programming
# 1. Create a DP table with size of n x n, with n = length of the string
# 2. Fill the diagonal with True
# 3. Starting from the backward, iterate the outer loop backwards and iterate the inner loop forward
# 4. Check characters at i and j position, if the 2 characters matches, 2 conditions need to be checked:
#    a. First, to see if j - i == 1
#    b. See if dp[i+1][j-1] == True

def longestPalindrome(s):
    longest_palin = ''
    # initialize matrix
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        longest_palin = s[i]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j - i == 1 or dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if len(longest_palin) < len(s[i:j+1]):
                        longest_palin = s[i:j+1]
    return longest_palin


s = 'eabcb'
print(longestPalindrome(s))
