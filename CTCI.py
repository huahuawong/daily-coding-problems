# This file contains solutions to the questions that are asked in Cracking the Coding Interview

# pg.82 
# Given a smaller string 5 and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation

# function to check if the string is permutation
def is_permutation(first, second):
    return sorted(first) == sorted(second)

# find the position of the permutations using sliding window method
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    """
    pos = []
    for pos1 in range(len(s1), len(s2) + 1):
        window_string = s2[pos1 - len(s1): pos1]
        if is_permutation(window_string, s1):
            pos.append(pos1 - len(s1))
    return pos


s1 = "ab"
s2 = "cdvab"
print(checkInclusion(s1, s2))

# The runtime complexity should be 0(n), where n is the length of s2 - length of s1. The permutation function should be running O(1), so it wouldn't affect
# the runtime


