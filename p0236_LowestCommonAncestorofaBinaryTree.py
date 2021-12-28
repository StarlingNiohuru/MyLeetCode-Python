class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# post order traverse
class Solution:
    p = None
    q = None

    def postOrder(self, node: TreeNode):
        if not node:
            return None
        if node == self.p or node == self.q:
            return node
        left = self.postOrder(node.left)
        right = self.postOrder(node.right)
        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
        else:
            return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p, self.q = p, q
        return self.postOrder(root)
