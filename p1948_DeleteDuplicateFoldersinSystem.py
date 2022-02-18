from collections import defaultdict

from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


# Trie and hash map of serialize key the node
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        node_map = defaultdict(list)
        temp_path, res = [], []

        def serialize(node: TrieNode):
            nonlocal node_map
            clist = [ch + serialize(child) for ch, child in node.children.items()]
            key = "(" + "".join(clist) + ")"
            if key != "()":
                node_map[key].append(node)
            return key

        def dfs(node: TrieNode):
            nonlocal temp_path, res
            if node.is_end:
                return
            elif len(temp_path) > 0:
                res.append(temp_path.copy())
            for key in node.children:
                temp_path.append(key)
                dfs(node.children[key])
                temp_path.pop()

        root = TrieNode()
        for path in sorted(paths):  # must sort the path here
            curr = root
            for c in path:
                curr = curr.children[c]

        serialize(root)
        for v in node_map.values():
            if len(v) > 1:
                for curr in v:
                    curr.is_end = True
        dfs(root)
        return res
