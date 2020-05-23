# Q1 You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called 
# flip, which changes a single x to y or vice versa.

# Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the 
# preceding example, it suffices to flip the second and sixth characters, so you should return 2.

def number_flips(string):
    strlen = len(string)
    # The idea is to get the last x positions in the string and
    # the first y position in the string because x precedes y
    first_y_position = 1
    last_x_position = -1
    for i in range(strlen):
        if string[i] == 'y':
            first_y_position = i
            break
    for i in range(strlen):
        index = strlen - i -1
        if string[index] == 'x':
            last_x_position = index
            break
    
    # Now we count how many number of flips we would need if we decide
    # to flip "y" to "x" from the string[0] to string[last_x_position] vs when we flip
    # "x" to "y" from first_y_position to the end of the string (i.e. len(string)
    x_count, y_count = 0, 0
    for i in range(first_y_position + 1, strlen):
        if string[i] == 'x':
            x_count += 1
    for i in range(last_x_position):
        if string[i] == 'y':
            y_count += 1
    return min(x_count, y_count)
    

print(number_flips("xyxyyyxyy"))
