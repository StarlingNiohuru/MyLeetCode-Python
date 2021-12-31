class Solution:
    def modifyString(self, s: str) -> str:
        res = ""
        for i, c in enumerate(s):
            if c == "?":
                prev = res[i - 1] if i > 0 else ""  # use res[i-1] to handle consecutive case like "de???bd"
                cons = s[i + 1] if i < len(s) - 1 else ""
                for x in "abc":
                    if x != prev and x != cons:
                        res += x
                        break
            else:
                res += c
        return res
