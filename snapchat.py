# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

# To approach this problem, it can be broken down into a couple of steps
# 1. Initialize an array to indicate the time for each lectures, the length would be the maximum value of the given array
# 2. Loop through the array and indicate the classroom times but assigning +1 for the start and -1 for the end.
# 3. Create two variables, rooms and temps, rooms to count number of rooms, temps to store the number of rooms in use as we calculate. Rooms update as tmps increments, i.e. if tmpps > room

# For example, let's say we have a given array of n = [(0, 2), (2, 4), (3, 5), (6, 9)].
# From step 1: the array would look like [1, 0, 0, 1, -1, -1, 1, 0, 0, -1]
# As we proceed to step 2 and step 3, we would notice that we need 2 rooms


import numpy as np


def find_num_classroom(n):
    if len(n) == 1:
        return 1
    max_num = np.max(n)
    time_counter = [0 for i in range(max_num+1)]

    for slots in n:
        time_counter[slots[0]] += 1
        time_counter[slots[1]] -= 1

    room, tmps = 0, 0

    for i in time_counter:
        # to see how many rooms are in use, +1 and -1 to indicate beginning and the end of session
        tmps += i
        # if tmps is higher than room, that means that we need additional rooms, hence room = tmps
        if tmps > room:
            room = tmps
    return room

  
print (solution([[30, 75], [0, 50], [60, 150]]))
print (solution([[30, 75], [0, 50], [60, 150], [30, 75]]))
print (solution([[(0, 2), (2, 4), (3, 5), (6, 9)]]))


