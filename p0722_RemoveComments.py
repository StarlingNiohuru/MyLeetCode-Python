from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_comment = False
        temp = ""
        for line in source:
            i, m = 0, len(line)
            while i < m:
                if i < m - 1 and not in_comment and line[i: i + 2] == "//":
                    break
                elif i < m - 1 and not in_comment and line[i: i + 2] == "/*":
                    in_comment = True
                    i += 1
                elif i < m - 1 and in_comment and line[i: i + 2] == "*/":
                    in_comment = False
                    i += 1
                elif not in_comment:
                    temp += line[i]
                i += 1
            if temp and not in_comment:
                res.append(temp)
                temp = ""
        return res
