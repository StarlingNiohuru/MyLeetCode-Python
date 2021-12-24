class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0 or carry > 0:
            temp = (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0) + carry
            carry = temp // 10
            temp %= 10
            res = str(temp) + res
            i -= 1
            j -= 1
        return res
