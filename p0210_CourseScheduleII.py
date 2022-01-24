from collections import deque
from typing import List


# Topological Sort of graph. BFS of nodes with inDegree==0
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1
        q = deque()
        for i, d in enumerate(inDegree):
            if d == 0:
                q.append(i)
        res = []
        while len(q) > 0:
            i = q.popleft()
            res.append(i)
            for j in adj[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)
        if len(res) < numCourses:
            res.clear()
        return res
