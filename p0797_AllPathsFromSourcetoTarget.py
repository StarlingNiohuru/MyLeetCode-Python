from typing import List


# dfs
class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        curr = []
        n = len(graph)

        def dfs(label):
            nonlocal res, curr, graph, n
            curr.append(label)
            if label == n - 1:
                res.append(curr.copy())
            else:
                for i in graph[label]:
                    dfs(i)
            curr.pop()

        dfs(0)
        return res
