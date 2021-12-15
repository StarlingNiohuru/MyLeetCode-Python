from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build a Graph and BFS from k (with a ghost node above k)
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        graph[None] = [k]
        graph[root.val].append(None)
        q.append(k)
        visited = set()
        while q:
            v = q.popleft()
            visited.add(v)
            if len(graph[v]) == 1:
                return v
            else:
                for i in graph[v]:
                    if i and i not in visited:
                        q.append(i)
