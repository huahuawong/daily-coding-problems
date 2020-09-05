# pg.82 
# Given a smaller string 5 and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation


def is_permutation(first, second):
    return sorted(first) == sorted(second)


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    pos = []
    for pos1 in range(len(s1), len(s2) + 1):
        window_string = s2[pos1 - len(s1): pos1]
        if is_permutation(window_string, s1):
            pos.append(pos1 - len(s1))

    return pos


s1 = "ab"
s2 = "cdvab"
print(checkInclusion(s1, s2))




