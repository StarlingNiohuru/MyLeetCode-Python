from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# DFS. mark '#' after every loop of children
class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ""
        vlist = [str(root.val)]
        for node in root.children:
            vlist.append(self.serialize(node))
        vlist.append("#")
        return ','.join(vlist)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        q = deque(data.split(','))
        root = Node(val=int(q.popleft()), children=[])

        def dfs(node):
            nonlocal q
            if len(q) == 0 or not node:
                return
            while q[0] != "#":
                child = Node(val=int(q.popleft()), children=[])
                node.children.append(child)
                dfs(child)
            q.popleft()

        dfs(root)
        return root
