def knows(a: int, b: int) -> bool:
    return


# brute force. TLE
class Solution:

    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    break
            else:
                return i
        return -1
