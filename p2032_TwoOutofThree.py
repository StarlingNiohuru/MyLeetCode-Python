from collections import defaultdict
from typing import List


# hash set and map
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        count = defaultdict(int)
        for k in s1:
            count[k] += 1
        for k in s2:
            count[k] += 1
        for k in s3:
            count[k] += 1
        res = []
        for k in count:
            if count[k] > 1:
                res.append(k)
        return res
