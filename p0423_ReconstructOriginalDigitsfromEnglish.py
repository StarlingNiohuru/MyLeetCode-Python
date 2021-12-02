import string


class Solution:
    def originalDigits(self, s: str) -> str:
        freq = {k: 0 for k in string.ascii_lowercase}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        digits = [0 for _ in range(10)]
        digits[0] = freq['z']
        digits[2] = freq['w']
        digits[4] = freq['u']
        digits[6] = freq['x']
        digits[8] = freq['g']
        digits[3] = freq['h'] - digits[8]
        digits[5] = freq['f'] - digits[4]
        digits[7] = freq['s'] - digits[6]
        digits[9] = freq['i'] - digits[5] - digits[6] - digits[8]
        digits[1] = freq['n'] - digits[7] - 2 * digits[9]
        res = ""
        for i, d in enumerate(digits):
            for _ in range(d):
                res += str(i)
        return res
