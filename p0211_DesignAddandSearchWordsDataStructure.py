from collections import defaultdict


# trie and dfs
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.trie_root = TrieNode()
        self.word = None
        self.res = None

    def addWord(self, word: str) -> None:
        curr = self.trie_root
        for c in word:
            curr = curr.children[c]
        curr.is_end = True

    def dfs(self, i: int, node: TrieNode):
        if not node:
            return
        if i == len(self.word):
            if node.is_end:
                self.res = True
            return
        if self.word[i] == ".":
            for child in node.children.values():
                self.dfs(i + 1, child)
        else:
            self.dfs(i + 1, node.children.get(self.word[i]))

    def search(self, word: str) -> bool:
        self.word = word
        self.res = False
        self.dfs(0, self.trie_root)
        return self.res
