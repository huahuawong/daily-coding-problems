# Q1 Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.

# For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.
MAXN = 105  # assume maximum value of n here

# dp[i] = number of max heaps for i distinct integers
dp = [0] * MAXN # intiialize dp arrays

# nck[i][j] = number of ways to choose j elements
#             from i elements, no order 
nck = [[0 for i in range(MAXN)] for j in range(MAXN)]

# log2[i] = floor of logarithm of base 2 of i, height of tree is always log2[i]
log2 = [0] * MAXN

# to calculate nCk， from n choose k elements
def choose(n, k):
    if (k > n):
        return 0
    if (n <= 1):
        return 1
    if (k == 0):
        return 1

    if (nck[n][k] != -1):
        return nck[n][k]

    answer = choose(n - 1, k - 1) + choose(n - 1, k)
    nck[n][k] = answer
    return answer


# calculate l for give value of n
def getLeft(n):
    if (n == 1):
        return 0

    h = log2[n]

    # max number of elements that can be present in the
    # hth level of any heap
    numh = (1 << h)  # (2 ^ h)

    # number of elements that are actually present in
    # last level(hth level)
    # (2^h - 1)
    last = n - ((numh) - 1)

    # if more than half-filled
    if (last >= (numh // 2)):
        return (1 << h) - 1  # (2^h) - 1
    else:
        return (1 << h) - 1 - ((numh // 2) - last)

    # find maximum number of heaps for n


def numberOfHeaps(n):
    if n <= 1:
        return 1

    left = getLeft(n)
    ans = (choose(n - 1, left) * numberOfHeaps(left)) * (numberOfHeaps(n - 1 - left))
    dp[n] = ans
    return ans


# function to initialize arrays
def solve(n):
    for i in range(n + 1):
        dp[i] = -1

    for i in range(n + 1):
        for j in range(n + 1):
            nck[i][j] = -1

    currLog2 = -1
    currPower2 = 1

    # for each power of two find logarithm
    for i in range(1, n + 1):
        if (currPower2 == i):
            currLog2 += 1
            currPower2 *= 2
        log2[i] = currLog2
    return numberOfHeaps(n)


# Driver code
n = 4
print(solve(n))







