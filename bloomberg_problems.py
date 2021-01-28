# Q1 Determine whether there exists a one-to-one character mapping from one string s1 to another s2

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

