from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        imax, jmax = height[i], height[j]
        res = 0
        while i < j:
            if height[i] < height[j]:
                res += max(imax - height[i], 0)
                imax = height[i] if height[i] > imax else imax
                i += 1
            else:
                res += max(jmax - height[j], 0)
                jmax = height[j] if height[j] > jmax else jmax
                j -= 1
        return res
