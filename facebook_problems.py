# 1 This problem was asked by Facebook.

# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.

#Note: not sure if this is unsigned or signed, probably doesn't matter because we are just reversing it

def reverse32(x)
    i = bin(i)                         # convert decimal to binary 
    i = i[2:]                          # discard the 0b
    i_reversed = i[::-1]               # reverse the number
    
    return i_reversed
    
# Driver code
 x = 100
 
 
# 2 In chess, the Elo rating system is used to calculate player strengths based on game results.
#
# A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent
# game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely
# the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than
# for beating a 1300-ranked player.
#
# Implement this system.


class EloRatings:
    # starting points of each user
    START_RATING = 1000

    # simple initialization
    def __init__(self):
        # dictionary is used to store the key(user name) and values (ratings based on win and loss)  of data
        self.ratings = dict()

    # add user name to dctionary
    def add_player(self, name):
        self.ratings[name] = EloRatings.START_RATING

    def add_result(self, p1, p2, winner):
        # In case the players haven't been added into the system yet
        if p1 not in self.ratings:
            self.add_player(p1)
        if p2 not in self.ratings:
            self.add_player(p2)

        # loser is p2 if the winner is p1, else the loser is p1
        loser = p2 if winner == p1 else p1
        # the loser rating will reduce by 10%, note that this means if user with higher score loses at one round, the winner will
        # get more points since the "diff" is based on the higher score percentage
        diff = self.ratings[loser] // 10
        self.ratings[loser] -= diff
        self.ratings[winner] += diff


# Tests
elo = EloRatings()
elo.add_player("a")
elo.add_player("b")
elo.add_result("a", "b", "a")
elo.ratings


# 3 
# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

# Analysis: Sounds simple, but the trick is we can only use mathematical operations, otherwise I'd use "if-else" statement. To proceed, let's define an equation
# to return either x and y, if its b = 1, we'll return 1 * x, and to mask y, we can just use abs(b-1) = abs (1-1) = 0. 
def find_integer(x, y, b):
    return x * b + y * abs(b-1)


x = 3; y = 5; b = 1
print(find_integer(x, y, b))

# 4 Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
from itertools import combinations  
import numpy as np

def find_prod(arr, n):
    pairs_array = list(combinations(arr, n))
    biggest = 0

    for pair in pairs_array:
        curr_mult = np.prod(pair)
        biggest = max(biggest, curr_mult)
    return biggest

arr = [-10, -10, 5, 4]; n = 3
print(find_prod(arr, n))


# 5 This problem was asked by Facebook.

# Implement regular expression matching with the following special characters:
#     . (period) which matches any single character
#     * (asterisk) which matches zero or more of the preceding element

# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" 
# should return false.

# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats"
# should return false.





# 6 Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.

# 1. Brute force approach
import itertools
import numpy as np

def find_max_prod(arr):
    max_prod = 0

    for i in itertools.permutations(arr, 3):
        # print(i)
        # print(np.prod(i))
        prod = np.prod(i)
        if max_prod < prod:
            max_prod = prod
    return max_prod

arr = [-10, -10, 5, 2]
find_max_prod(arr)

# 2. We know that if given a sorted array, the biggest prod will either be the product of 2 smallest integer (assuming
# negative number) and the largest number (rightmost number) or the 3 largest numbers from the right

def find_max_prod(arr):
    arr.sort()    
    return max((arr[0] * arr[1] * arr[-1]), arr[-1] * arr[-2] * arr[-3])


# 6 Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.



