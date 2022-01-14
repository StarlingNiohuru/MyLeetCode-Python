# Greedy. Always choose the valid char having the biggest count.
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        count = [['a', a], ['b', b], ['c', c]]
        while True:
            count.sort(reverse=True, key=lambda x: x[1])
            index = 1 if len(res) >= 2 and res[-1] == res[-2] == count[0][0] else 0
            if count[index][1]:
                res += count[index][0]
                count[index][1] -= 1
            else:
                break
        return res
