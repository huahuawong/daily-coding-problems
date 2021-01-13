# Q1 At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). 
# To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

# Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

# function to see if a knows b
def knows(known, a, b):
    return b in known[a]


def get_celeb(known):
    # set of keys from the known dataset
    celeb_candidates = set(known.keys())

    while celeb_candidates:
        # gets the next iterable candidates, notice that 
        sample = next(iter(celeb_candidates))
        celeb_candidates.remove(sample)
        count = len(celeb_candidates)
        for other in celeb_candidates:
            if not knows(known, sample, other):
                count -= 1
        if count == 0:
            return sample

known = {'a': {'b', 'c'},
         'b': {'c'},
         'c': {'a'},
         'd': set()}

print(get_celeb(known))

# Q2 Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
# Well this can be solved using the naive approach, which is to start from the first element and recursively call for all the elements reachable from first element. 
# An alternative approach is using dynamic programming to find the minimum jumps to get to the last index, If there is no minimum jumps to reach the end, then 
# it is unreachable

# Breakdown: 1. Check initial conditions and return False if condition is met
#            2. We initialize an empty jump array filled with zeroes and find number of steps to reach arr[i] from starting points
#            3. If i is less than j + arr[j] and the jump isn't infinity, then we append the step into jumps[i]
#            4. If it can't be reached, the last element would be inf, because of "jumps[i] = float('inf')
#            5. Else, it is true

def find_jumps(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0
    # Find the minimum number of jumps to reach arr[i] from
    # arr[0] and assign this value to jumps[i]

    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break

    if jumps[n-1] == float('inf'):
        return False
    return True


arr = [2, 2, 3, 5, 0, 0, 0, 0, 2]
# arr = [2, 0, 1, 0]
# arr = [1, 1, 0, 1]
print(find_jumps(arr, len(arr)))

