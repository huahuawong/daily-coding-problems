# This problem was asked by Stripe.
#
# Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
# For example, given 156, you should return 3

def cal_longest_run(num):
    binary_representation = "{0:b}".format(num)
    max_run = 0; curr_run = 0
    for i in range(0, len(binary_representation)):
        if binary_representation[i] == '1':
            curr_run += 1
            max_run = max(max_run, curr_run)

        if binary_representation[i] == '0':
            max_run = max(max_run, curr_run)
            curr_run = 0
    return max_run


assert cal_longest_run(156) == 3
assert cal_longest_run(55) == 3

num = 55
print(cal_longest_run(num))
