class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        res = ""
        while i >= 0 or j >= 0 or carry > 0:
            temp = (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0) + carry
            carry = temp // 2
            temp %= 2
            res = str(temp) + res
            i -= 1
            j -= 1
        return res
