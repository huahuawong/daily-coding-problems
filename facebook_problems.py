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








