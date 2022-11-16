# Link to the problem: https://leetcode.com/problems/valid-parentheses/

# A quick and easy way is to initialize two list, one for "left", one for "right"
# And as we go through the string, we can check if its in the left or right, at the end of the day if it is not valid, then we wouldnt have an empty string, if so, return False


def isValid(self, s: str) -> bool:
    left =  ['(', '[', '{']
    right = [')', ']', '}']

    if len(s) % 2 != 0:
        return False

    if s[0] in right:
        return False

    check_arr = []

    for character in s:
        if character in left:
            check_arr.append(left.index(character))
        else:
            if len(check_arr) == 0:
                # print("False")
                return False
            right_index = right.index(character)

            if check_arr[-1] == right_index:
                check_arr.pop()
            else:
                return False

    return (len(check_arr) == 0)
