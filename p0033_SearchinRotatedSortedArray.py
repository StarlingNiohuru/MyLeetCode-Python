from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        pivot = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            old_mid = (pivot + mid) % len(nums)
            if nums[old_mid] > target:
                hi = mid - 1
            elif nums[old_mid] < target:
                lo = mid + 1
            else:
                return old_mid
        return -1
