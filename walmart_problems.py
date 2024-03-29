# There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are no gaps between any of them, while keeping 
# overall movement to a minimum.

# For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty seat and 1 represents a person. In this case, 
# one solution would be to place the person on the right in the fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each
# person must move, so that the cost here would be five.

# Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.

# Initial idea is to find all indexes where the index is 1, and from then we would assume each 1 as a "focal point" that other 1s would have to move to, calculate for
# each 1 index and then return the minimum
