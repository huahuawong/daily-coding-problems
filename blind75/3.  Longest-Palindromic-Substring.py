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
