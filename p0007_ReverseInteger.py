class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x >= 0 else -1
        n = abs(x)
        while n > 0:
            res = res * 10 + n % 10
            n //= 10
        res *= sign
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            res = 0
        return res
