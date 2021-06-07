# Q1. LC 1119 Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
import re


def strip_vowels(word):
    return re.sub("[AEIOUaeiou]", "", word)

# Q2. LC 1165 Single Row Keyboard
# There is a special keyboard with all keys in a single row.
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your
# finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
# The time taken to move your finger from index i to index j is |i - j|.
#
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.


def find_count(keyboard, word):
    count = 0; cur_pos = 0

    for i in word:
        index = keyboard.index(i)
        if cur_pos < index:
            count += index - cur_pos
            cur_pos = index
        elif cur_pos > index:
            count += cur_pos - index
            cur_pos = index
    return count

# OR,


def find_count(keyboard, word):
    d = {char: idx for idx, char in enumerate(keyboard)}
    total_time = prior_idx = 0
    for char in word:
        idx = d[char]
        total_time += abs(idx - prior_idx)
        prior_idx = idx
    return total_time


# Q3 LC 1614. Maximum Nesting Depth of the Parentheses
# A string is a valid parentheses string (denoted VPS) if it meets one of the following:
#
# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
#
# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
#
# Given a VPS represented as string s, return the nesting depth of s.
#
def find_depth(word):
    max_depth = curr_depth = 0
    d = {'(': 1, ')': -1}
    for character in word:
        curr_depth += d.get(character, 0) # returns 0 if no match is found so no change to the depth
        max_depth = max(max_depth, curr_depth)

# Note, Similar problems:
# 22. Generate Parentheses
# 32. Longest Valid Parentheses
# 241. Different Ways to Add Parentheses
# 301. Remove Invalid Parentheses
# 678. Valid Parenthesis String
# 856. Score of Parentheses
# 921. Minimum Add to Make Parentheses Valid
# 1021. Remove Outermost Parentheses
# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# 1190. Reverse Substrings Between Each Pair of Parentheses
# 1249. Minimum Remove to Make Valid Parentheses
# 1541. Minimum Insertions to Balance a Parentheses String


# Q4 LC 20 Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid. An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Input: s = "()[]{}"
# Output: true

def valid_paran(s):
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


# Q5 Roman to Integers
def roman_to_int(s):
    count = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(s) - 1):
        if dict[s[i]] < dict[s[i+1]]:
            count -= dict[s[i]]
        else:
            count += dict[s[i]]

    return (count + dict[s[-1]])
