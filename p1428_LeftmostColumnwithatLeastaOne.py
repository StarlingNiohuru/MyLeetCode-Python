class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:

    def dimensions(self) -> list[]:


# Binary search vertically.
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            one_exist = False
            for i in range(m):
                if binaryMatrix.get(i, mid):
                    one_exist = True
                    break
            if one_exist:
                hi = mid
            else:
                lo = mid + 1
        res = lo if lo < n else -1
        return res
