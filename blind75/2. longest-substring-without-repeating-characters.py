# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# 'Sliding window' way
def find_longest_substring(s):
    window = []; max_len = 0
    for i in range(0, len(s)):
        if not s[i] in window:
            window.append(s[i])
            continue
        if s[i] in window:
            if window[0] == s[i]:
                max_len = max(max_len, len(window))
                window.pop(0)
                window.append(s[i])
                continue
            else:
                max_len = max(max_len, len(window))
                window = []
                window.append(s[i])
                continue
    return max_len
  
  
  
# Alernative way
def find_longest_substring(s):
    start = max_len = 0
    string_dict = {}
    for i in range(len(s)):
        if s[i] in string_dict and start <= string_dict[s[i]]:
            start = string_dict[s[i]] + 1           
        else:
            max_len = max(max_len, i - start + 1)
        string_dict[s[i]] = i
    return max_len
               
