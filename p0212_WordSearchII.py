from collections import defaultdict
from typing import List


# Trie and dfs
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Solution:
    board = None
    m = None
    n = None
    trie_root = None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = []

    def buildTrie(self, words: List[str]):
        self.trie_root = TrieNode()
        for word in words:
            curr = self.trie_root
            for c in word:
                curr = curr.children[c]
            curr.is_end = True  # avoid duplicate

    def dfs(self, i: int, j: int, prefix: str, node: TrieNode):
        temp = self.board[i][j]
        prefix += temp
        if not node:
            return
        elif node.is_end:
            self.res.append(prefix)
            node.is_end = False
        self.board[i][j] = "#"
        for d in self.directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] in node.children:
                self.dfs(x, y, prefix, node.children.get(self.board[x][y]))
        self.board[i][j] = temp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.buildTrie(words)
        self.res = []
        for i in range(self.m):
            for j in range(self.n):
                node = self.trie_root.children.get(board[i][j])
                self.dfs(i, j, "", node)
        return self.res
