from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a, b = j + 1, n - 1
                while a < b:
                    if a > j + 1 and nums[a] == nums[a - 1]:
                        a += 1
                        continue
                    sum4 = nums[i] + nums[j] + nums[a] + nums[b]
                    if sum4 == target:
                        res.append([nums[i], nums[j], nums[a], nums[b]])
                        a += 1
                        b -= 1
                    elif sum4 < target:
                        a += 1
                    else:
                        b -= 1
        return res
