from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, count, = 0, 0
        for j in range(len(chars)):
            count += 1
            if j == len(chars) - 1 or chars[j] != chars[j + 1]:
                chars[i] = chars[j]
                i += 1
                if count > 1:
                    for s in str(count):
                        chars[i] = s
                        i += 1
                count = 0
        chars = chars[:i]
        res = len(chars)
        return res
