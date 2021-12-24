from typing import List


# hash map with index:value
class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = {}
        for i in range(len(nums)):
            if nums[i]:
                self.non_zeros[i] = nums[i]

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k, v in self.non_zeros.items():
            if k in vec.non_zeros:
                res += v * vec.non_zeros[k]
        return res
