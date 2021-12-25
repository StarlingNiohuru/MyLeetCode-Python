from typing import List


# pre product from both sides
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, front, back = [], [1], [1]
        for i in range(n):
            front.append(front[-1] * nums[i])
            back.append(back[-1] * nums[n - 1 - i])
        for i in range(n):
            res.append(front[i] * back[n - 1 - i])
        return res
