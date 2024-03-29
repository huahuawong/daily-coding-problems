# Q1 This problem was asked by Twitter.

# A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 
# 16891 is strobogrammatic.

# Create a program that finds all strobogrammatic numbers with N digits.
def get_strob(n_digits):
    if not n_digits:
        return [""]
    elif n_digits == 1:
        return ['0', '1', '8']
        
    small_numbers = get_strob(n_digits-2)
    list_of_small = list()
    for num in small_numbers:
        list_of_small.extend([
            "1" + num + "1",
            "6" + num + "9",
            "9" + num + "6",
            "8" + num + "8",
        ])
    return list_of_small
    
print(get_strob(3))
        
# Q2 This problem was asked by Twitter.
# The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value 24.
# For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.
# Write a function that plays the 24 game.
OPERATORS = {'+', '-', '*', '/'}
TARGET = 24


def possible(arr):
    # Check if it is just of one length, if it is it has to be 24 or else it is False
    if len(arr) == 1:
        return arr[0] == TARGET

    # initialize list to store all possibilities after doing arithmetic calculations
    new_possibilities = list()

    # Generating all possibilities of the operations
    for si in range(len(arr) - 1):
        for operator in OPERATORS:
            num_1 = arr[si]
            num_2 = arr[si + 1]
            try:
                possibility = arr[:si] + [eval("{}{}{}".format(num_1, operator, num_2))] + arr[si + 2:]
                new_possibilities.append(possibility)
            except Exception:
                pass

    return any([possible(x) for x in new_possibilities])


# This problem was asked by Twitter.

# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
# Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].


arr = ["a", "b", "c", "a", "s"]         # ["a", "b", "c"]

num_dict = {}

for ele in enumerate(arr):
    num_dict[ele[0]] = ele[1]
    
print(num_dict)

ordered_arr = [2, 1, 0, 3, 4]

rearranged_arr = []

for num in ordered_arr:
    rearranged_arr.append(num_dict[num])
    
print(rearranged_arr)

# A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

# {0: [1, 2],
#  1: [0, 5],
#  2: [0],
#  3: [6],
#  4: [],
#  5: [1],
#  6: [3]} 
# Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.


