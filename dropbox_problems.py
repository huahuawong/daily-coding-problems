# Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
# Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

import string
alpha = list(string.ascii_lowercase)

def num_hash(n):
    if n < 26:
        return alpha[n-1]
    else:
        quotient, remainder = n//26, n%26
        if remainder == 0:
            if quotient == 1:
                return alpha[remainder - 1]
            else:
                return num_hash(quotient - 1) + alpha[remainder - 1]
        else:
            return num_hash(quotient) + alpha[remainder - 1]    
    
    
n = 702
print(num_hash(n))

# 2 Given a string s and a list of words words, where each word is the same length, find all starting indices of
# substrings in s that is a concatenation of every word in words exactly once.
#
# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at
# index 0 and "catdog" starts at index 13.
#
# Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog"
# and "cat" in s.

import itertools

words = ["cat", "dog"]
s = "dogcatcatcodecatdog"
# s = "barfoobazbitbyte"

def find_starting_index(s, words):
    possible_words = list(itertools.permutations(words))

    possible_concats = []

    for word in possible_words:
        possible_concats.append(''.join(word))

    index_arr = []
    for word in possible_concats:
        index = s.find(word)
        if index == -1:
            return []
        index_arr.append(index)
    return index_arr


print(find_starting_index(s, words))
