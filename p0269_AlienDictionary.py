from collections import deque, defaultdict
from typing import List


# Topological Sort of graph of chars. Compare adjacent words in word list to build graph. BFS of nodes with inDegree==0
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        inDegree = defaultdict(int)
        adj = defaultdict(list)
        chars = set()
        for word in words:
            for c in word:
                if c not in chars:
                    chars.add(c)
                    inDegree[c] = 0
                    adj[c] = []
        for i in range(1, len(words)):
            first, second = words[i - 1], words[i]
            for j in range(min(len(first), len(second))):
                a, b = first[j], second[j]
                if a != b:
                    adj[a].append(b)
                    inDegree[b] += 1
                    break
            else:
                if len(first) > len(second):
                    return ""
        q = deque()
        for k in inDegree:
            if inDegree[k] == 0:
                q.append(k)
        res = ""
        while len(q) > 0:
            c = q.popleft()
            res += c
            for j in adj[c]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)
        if len(res) < len(chars):
            res = ""
        return res
