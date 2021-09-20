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
