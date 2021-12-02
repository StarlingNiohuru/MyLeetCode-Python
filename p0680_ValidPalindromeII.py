class Solution:
    def _vaildPalindrome1(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self._vaildPalindrome1(s[i:j]) or self._vaildPalindrome1(s[i + 1:j + 1])
            else:
                i += 1
                j -= 1
        return True
