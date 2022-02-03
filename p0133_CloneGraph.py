class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# DFS and hash map of pairs {old:new}
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(curr: 'Node'):
            nonlocal visited
            if not curr:
                return
            visited[curr] = Node(curr.val)
            for neigh in curr.neighbors:
                if neigh not in visited:
                    dfs(neigh)
                visited[curr].neighbors.append(visited[neigh])

        dfs(node)
        return visited[node] if node else None
