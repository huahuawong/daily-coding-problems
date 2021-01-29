# Q1 Determine whether there exists a one-to-one character mapping from one string s1 to another s2
# We need to first understand the question, we want to find a one-to-one relationship, does not necessarily have to be in alphabetical order.
# To solve this problem, essentially we can initialize two empty dict, and append elements from the other array if the element is not in the dict and the value of the key 
# has the same value. Returns False if the element is present in the dictionary AND the value of the key is different from the element at index i
def isIsomorphic(s, t):
    s2t, t2s = {}, {}
    for i in range(len(s)):
        if s[i] in s2t and s2t[s[i]] != t[i]:
            return False
        if t[i] in t2s and t2s[t[i]] != s[i]:
            return False
        s2t[s[i]] = t[i]
        t2s[t[i]] = s[i]
    return True


str1 = "aab"; str2 = "xyy"
print(isIsomorphic(str1, str2))

