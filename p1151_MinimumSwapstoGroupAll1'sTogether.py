from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_count = sum(data)
        sub_count, max_count = 0, 0
        for i in range(len(data)):
            if i < total_count:
                sub_count += data[i]
            else:
                sub_count += data[i] - data[i - total_count]
            max_count = max(max_count, sub_count)
        res = total_count - max_count
        return res
