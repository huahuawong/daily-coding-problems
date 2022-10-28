# Full description on the question: https://leetcode.com/problems/container-with-most-water/


def maxArea(self, height: List[int]) -> int:
    ans = 0
    i = 0; j = len(height) - 1

    while (i < j):
        if height[i] < height[j]:
            res = height[i] * (j-i)
            i += 1
        else:
            res = height[j] * (j-i)
            j -= 1
        ans = max(res, ans)
    return ans
