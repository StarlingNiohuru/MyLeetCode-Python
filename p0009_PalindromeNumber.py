class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        temp = 0
        while x > temp:
            temp = temp * 10 + x % 10
            x //= 10
        return x == temp or x == (temp // 10)


# int to string
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s) - 1
        for i in range(0, (n + 1) // 2):
            if s[i] != s[n - i]:
                return False
        return True
