# Q1 Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until
# reaching the kth line, then back up to top right, and so on.

# Solution ref: https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_253.py

# 1. Intiialize a dictionary with 4 keys. Each key will represent the rows of the end result. {0:'', 1:'', 2:'', 3:''}
# 2. Initialize 2 variables, direction to indicate if its going up or down, and crow, which indicates column of that row.
# 3. Let's say the word is "thisisazigzag" and k = 4, for the first iteration downward the zigzag, "t" is placed in first key in the dict,
# For the second character "h", direction will be flipped to +1, and crow will now be 1, so "h" will be placed in second key in the dict.
# Keep repeating until crow == k-1 or crow == 0, direciton will be changed to -1, and naturally crow will start decrmenting from 3 to 2, so the new char will be placed in the third 
# key {2: }
# 4. Repeat this and print it by placeing "\n" between each key's values

def print_zigzag(string, k):

    string_dict = dict()
    for row in range(k):
        string_dict[row] = ""

    crow = 0
    direction = -1
    for i in range(len(string)):
        for row in range(k):
            if row == crow:
                string_dict[row] += string[i]
            else:
                string_dict[row] += " "

        if crow == k-1 or crow == 0:
            direction *= -1

        crow += direction

    final_string = "\n".join([x for x in string_dict.values()])

    print(final_string)
