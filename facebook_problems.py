#1 This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.

#Note: not sure if this is unsigned or signed, probably doesn't matter because we are just reversing it

def reverse32(x)
    i = bin(i)                         # convert decimal to binary 
    i = i[2:]                          # discard the 0b
    i_reversed = i[::-1]               # reverse the number
    
    return i_reversed
    
# Driver code
 x = 100
 
 
#2 In chess, the Elo rating system is used to calculate player strengths based on game results.
#
# A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent
# game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely
# the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than
# for beating a 1300-ranked player.
#
# Implement this system.




