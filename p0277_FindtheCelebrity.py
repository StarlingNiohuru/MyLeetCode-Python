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


# In the graph matrix, celebrity has all 1 col and all 0 row.
# From (0,n-1) search the candidate on the diagonal and verify it.
class Solution2:

    def findCelebrity(self, n: int) -> int:
        i, j = 0, n - 1
        while i < j:
            if knows(i, j):
                i += 1
            else:
                j -= 1
        for k in range(n):
            if k == i:
                continue
            if knows(i, k) or not knows(k, i):
                return -1
        return i
