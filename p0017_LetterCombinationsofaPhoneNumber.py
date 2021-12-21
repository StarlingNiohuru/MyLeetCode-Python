from typing import List


class Solution:
    dmap = None
    digits = ""
    res = None

    def dfs(self, i: int, temp: str):
        if i == len(self.digits):
            if i > 0:
                self.res.append(temp)
            return
        for c in self.dmap[self.digits[i]]:
            self.dfs(i + 1, temp + c)

    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        self.digits = digits
        self.dmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.dfs(0, "")
        return self.res
