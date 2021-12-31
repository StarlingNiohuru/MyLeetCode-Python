class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs
class Codec:
    data = []
    index = None

    def serialize(self, root):
        if not root:
            return "#"
        return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def dfs(self):
        if self.index == len(self.data):
            return
        self.index += 1
        if self.data[self.index] == "#":
            return
        node = TreeNode(int(self.data[self.index]))
        node.left = self.dfs()
        node.right = self.dfs()
        return node

    def deserialize(self, data):
        self.data = data.split(',')
        self.index = -1
        return self.dfs()
