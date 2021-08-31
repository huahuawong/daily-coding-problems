# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

# To approach this problem, it can be broken down into a couple of steps
# 1. Initialize an array to indicate the time for each lectures, the length would be the maximum value of the given array
# 2. Loop through the array and indicate the classroom times but assigning +1 for the start and -1 for the end.
# 3. Create two variables, rooms and temps, rooms to count


