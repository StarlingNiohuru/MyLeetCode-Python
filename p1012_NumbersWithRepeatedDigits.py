class Solution:
    def _permutation(self, n: int, k: int):
        res = 1
        for i in range(n, n - k, -1):
            res *= i
        return res

    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = str(n)
        unique_digits, digits_len = 0, len(digits)
        for i in range(digits_len - 1):
            unique_digits += 9 * self._permutation(9, i)
        used = set()
        for i in range(digits_len):
            d = int(digits[i])
            start = 0 if i else 1
            end = d + 1 if i == digits_len - 1 else d
            for j in range(start, end):
                if j not in used:
                    unique_digits += self._permutation(9 - i, digits_len - i - 1)
            if d in used:
                break
            used.add(d)
        res = n - unique_digits
        return res
