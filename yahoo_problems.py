# You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters 
# and moving it to the end.

# Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.
def newString(s, k): 
    
    if k == 1:
        min_ch = min(s)
        joined = s + s
        for i, ch in enumerate(joined):
            if ch == min_ch:
                return joined[i:i + len(s)]
    
    # new string 
    X = "" 
  
    # Remove characters until 
    # the string is empty 
    while (len(s) > 0): 
        temp = s[0] 
  
        # Traverse to find the smallest  
        # character in the first k characters 
        i = 1
        while(i < k and i < len(s)): 
            if (s[i] < temp): 
                temp = s[i] 
  
            i += 1
          
        # append the smallest character 
        X = X + temp 
  
        # removing the lexicographically  
        # smallest character from the string 
        for i in range(k): 
            if (s[i] == temp): 
                s = s[0:i] + s[i + 1:] 
                break
          
    return X

s = "daily"
k = 2
print(newString(s, k))




