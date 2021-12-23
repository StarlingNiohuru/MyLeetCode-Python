from typing import List


# hashmap with char:index
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        omap = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            j = 0
            while j < len(words[i - 1]) and j < len(words[i]):
                c1, c2 = omap[words[i - 1][j]], omap[words[i][j]]
                if c1 < c2:
                    break
                elif c1 > c2:
                    return False
                j += 1
            else:
                if len(words[i - 1]) > len(words[i]):
                    return False
        return True
