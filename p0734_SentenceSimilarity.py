from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        n = len(sentence1)
        for i in range(n):
            a, b = sentence1[i], sentence2[i]
            if a == b:
                continue
            elif [a, b] in similarPairs or [b, a] in similarPairs:
                continue
            else:
                return False
        return True
