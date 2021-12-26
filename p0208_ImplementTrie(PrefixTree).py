from collections import defaultdict


# defaultdict with TrieNode class
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie:

    def __init__(self):
        self.dummy = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.dummy
        for c in word:
            curr = curr.children[c]  # create a new TrieNode
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.dummy
        for c in word:
            curr = curr.children.get(c)  # won't create a new TrieNode
            if not curr:
                return False
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.dummy
        for c in prefix:
            curr = curr.children.get(c)
            if not curr:
                return False
        return True
