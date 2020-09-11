#1 Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Let's say we have 

s = "penapplepen"
words = ["apple", "pen"]

# Basically, the idea is:
# Initialize an array of False, length of array is same as the s    
# d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word
# d[2] is True because there is "pen" in the dictionary that ends at 2nd index of "penapplepen"
# d[7] is True because there is "apple" in the dictionary that ends at the 7th index of "leetcode" AND d[2] is True
# d[10] is True because there is "pen" in the dictionary that ends at the 10th index of "leetcode" AND d[7] is True

So the code goes:

def wordBreak(s, wordDict):
     d = [False] * len(s)
     for i in range(len(s)):
         for w in wordDict: 
             if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                 d[i] = True
     return d[-1]
        
        
#2 Given a string and a string dictionary, find the longest string in the dictionary that can be formed by 
# deleting some characters of the given string. If there are more than one possible results, return the longest word 
# with the smallest lexicographical order. If there is no possible result, return the empty string. 

def findlongestword(s, d):
     d.sort(key = lambda x: (-len(x), x)   #we first sort the words in d based on length in descending order,
                                             #followed by alphabets
     for word in d:
          i = 0
          for c in s:
               if i < len(word) and word [i] == c:
                    i += 1  # increment i
               if i == len(word):
                    return word      #if i equals to length of word, means that it has found the longest word
                    
     return ""


s = "abpcplea"
d = ["ale","apple","monkey","plea"]


#3 Integer to Roman conversion
def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num//val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
    
print(int_to_Roman(8))




