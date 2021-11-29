from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in index_map:
                return [index_map[complement], i + 1]
            else:
                index_map[numbers[i]] = i + 1
