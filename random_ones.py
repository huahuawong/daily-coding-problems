# Given a real number n, find the square root of n. For example, given n = 9, return 3

import numpy as np
print(np.sqrt(num))

# Assuming if we can't use this package to get square root, we can use another approach that uses binary search and recursion
# 1. First step is to initialize i and iterate until it reaches n, but we do i*i for each iteration
# 2. Stop when i*i > n, now we know the value we are looking at is between i-1 and i
# 3. That's when recursion and binary search come in, we will keep finding the mid between i-1 and i, and keep iterating for the 1st half or second half, depending on 
# the value of the mid
